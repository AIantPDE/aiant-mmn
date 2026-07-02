from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast


ROOT = Path(__file__).resolve().parents[2]

DOC_MD = (
    ROOT
    / "docs"
    / "verification"
    / "MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_PLAN_ALIGNMENT_V0.md"
)
DOC_JSON = (
    ROOT
    / "docs"
    / "verification"
    / "mmn_authority_event_memory_write_request_candidate_preview_plan_alignment_v0.json"
)
FIXTURE_JSON = (
    ROOT
    / "tests"
    / "fixtures"
    / "mmn_authority_event_memory"
    / "write_request_candidate_preview_plan_alignment_v0.json"
)


def _load_json(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return cast(dict[str, Any], payload)


def _dict(value: Any) -> dict[str, Any]:
    assert isinstance(value, dict)
    return cast(dict[str, Any], value)


def _list(value: Any) -> list[Any]:
    assert isinstance(value, list)
    return cast(list[Any], value)


def test_write_request_candidate_preview_alignment_docs_exist() -> None:
    assert DOC_MD.exists()
    assert DOC_JSON.exists()
    assert FIXTURE_JSON.exists()


def test_write_request_candidate_preview_alignment_payloads_match() -> None:
    assert _load_json(DOC_JSON) == _load_json(FIXTURE_JSON)


def test_alignment_keeps_preview_candidate_only() -> None:
    payload = _load_json(FIXTURE_JSON)

    assert payload["asset_kind"] == "write_request_candidate_preview_plan_alignment"
    assert payload["alignment_status"] == "aligned_candidate_only_with_deferral"
    assert payload["alignment_outcome"] == "keep_preview_plan_candidate_only"

    decision = _dict(payload["alignment_decision"])
    assert decision["preview_plan_v0_remains_valid_as_candidate_only"] is True
    assert decision["preview_plan_v0_requires_alignment_before_v1"] is True
    assert decision["formal_field_registry_promotion_allowed"] is False
    assert decision["runtime_authorization_allowed"] is False
    assert decision["memory_write_authority_allowed"] is False
    assert decision["default_on_unresolved_alignment_gap"] == "deny_fail_closed"


def test_alignment_trace_includes_business_and_contracts_deferral() -> None:
    payload = _load_json(FIXTURE_JSON)
    trace = _list(payload["alignment_trace"])
    artifacts = {_dict(step)["artifact"] for step in trace}

    assert "mmn business requirement scenario fixtures v0" in artifacts
    assert (
        "contracts candidate field registry promotion-or-deferral decision v0"
        in artifacts
    )
    assert "mmn write request candidate preview plan alignment v0" in artifacts

    statuses = {_dict(step)["authority_status"] for step in trace}
    assert "defer_formal_field_registry_promotion" in statuses
    assert "candidate_only_alignment" in statuses


def test_alignment_requires_updates_before_v1() -> None:
    payload = _load_json(FIXTURE_JSON)
    updates = _list(payload["required_alignment_updates_before_v1"])

    update_names = {_dict(update)["alignment_item"] for update in updates}
    assert "business_scenario_trace_refs" in update_names
    assert "field_feedback_resolution_refs" in update_names
    assert "requested_operation_and_scope_semantics" in update_names
    assert "revocation_and_expiry_evidence_refs" in update_names
    assert "trace_lineage_and_dedupe_fields" in update_names
    assert "forbidden_authority_claim_detection" in update_names

    for raw_update in updates:
        update = _dict(raw_update)
        assert update["status"] in {
            "required_before_v1",
            "required_before_runtime_claims",
            "required_before_accepted_surface_expansion",
        }
        assert update["reason"]


def test_all_business_scenarios_have_preview_alignment() -> None:
    payload = _load_json(FIXTURE_JSON)
    alignments = _list(payload["scenario_to_preview_alignment"])

    assert len(alignments) == 9

    scenario_ids = {_dict(item)["scenario_id"] for item in alignments}
    assert "grant_scope_mismatch_denial" in scenario_ids
    assert "revocation_or_expiry_evidence_required" in scenario_ids
    assert "duplicate_write_candidate_dedupe_required" in scenario_ids
    assert "candidate_payload_authorization_claim_denied" in scenario_ids
    assert "drl_trading_or_future_live_claim_denied" in scenario_ids

    for raw_alignment in alignments:
        alignment = _dict(raw_alignment)
        assert alignment["preview_plan_alignment"]
        assert alignment["alignment_result"]
        assert _list(alignment["required_candidate_fields"])


def test_alignment_non_authorizations_are_false() -> None:
    payload = _load_json(FIXTURE_JSON)
    non_auth = _dict(payload["required_non_authorizations"])

    required_keys = {
        "write_request_schema_authorized",
        "writeback_request_schema_authorized",
        "memory_record_schema_authorized",
        "formal_field_registry_update_authorized",
        "grant_decision_receipt_authorized",
        "memory_write_authority_granted",
        "runtime_topology_path_authorized",
        "runtime_shadow_mode_authorized",
        "drl_execution_authorized",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    }

    assert required_keys <= set(non_auth)
    assert all(value is False for value in non_auth.values())


def test_alignment_blocks_dangerous_interpretations() -> None:
    payload = _load_json(FIXTURE_JSON)
    blocked = set(_list(payload["blocked_interpretations"]))

    assert (
        "write request candidate preview plan v0 treated as write request schema"
        in blocked
    )
    assert "business scenario fixture treated as runtime shadow mode" in blocked
    assert "candidate field registry treated as authoritative field registry" in blocked
    assert "read-only projection treated as memory write authority" in blocked
    assert "core topology reference treated as runtime path enablement" in blocked
    assert "absence of revocation evidence treated as active authorization" in blocked


def test_alignment_markdown_states_candidate_only_boundaries() -> None:
    text = DOC_MD.read_text(encoding="utf-8")

    assert "keep_preview_plan_candidate_only" in text
    assert "defer_formal_field_registry_promotion" in text
    assert "candidate-only / preview-only" in text
    assert "本文档不授权" in text
    assert "future live execution" in text
