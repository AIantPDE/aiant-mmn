from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = (
    ROOT
    / "docs"
    / "verification"
    / "MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_FIXTURES_V1.md"
)
MANIFEST_PATH = (
    ROOT
    / "docs"
    / "verification"
    / "mmn_authority_event_memory_write_request_candidate_preview_fixtures_v1.json"
)
FIXTURE_PATH = (
    ROOT
    / "tests"
    / "fixtures"
    / "mmn_authority_event_memory"
    / "write_request_candidate_preview_fixtures_v1.json"
)

JsonDict = dict[str, Any]


def load_json_dict(path: Path) -> JsonDict:
    parsed = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(parsed, dict)
    return cast(JsonDict, parsed)


def test_write_request_candidate_preview_fixtures_v1_doc_declares_boundary() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    required_terms = [
        "write request candidate preview fixtures v1",
        "non-executing business requirement fixture",
        "preview-only",
        "fixture-only",
        "report-only",
        "not authority source",
        "memory write authority",
        "runtime shadow mode",
        "accepted schema surface expansion",
        "formal FIELD_REGISTRY update",
        "deny_fail_closed",
    ]

    missing = [term for term in required_terms if term not in text]
    assert missing == []


def test_manifest_and_fixture_share_candidate_identity() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    fixture = load_json_dict(FIXTURE_PATH)

    assert (
        manifest["asset_id"]
        == "mmn_authority_event_memory_write_request_candidate_preview_fixtures_v1"
    )
    assert manifest["asset_kind"] == "write_request_candidate_preview_fixtures"
    assert manifest["fixture_family_version"] == "v1"
    assert manifest["plan_status"] == "candidate_preview_fixture_only"
    assert manifest["candidate_outcome"] == "write_request_candidate_preview_fixtures_v1_only"

    for key in [
        "asset_id",
        "asset_kind",
        "fixture_family_version",
        "plan_status",
        "candidate_outcome",
    ]:
        assert fixture[key] == manifest[key]


def test_explicit_non_authorizations_remain_false() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    non_authorizations = cast(JsonDict, manifest["explicit_non_authorizations"])

    expected_false_keys = {
        "formal_grant_decision_receipt_authorized",
        "formal_write_request_schema_authorized",
        "accepted_schema_surface_expansion_authorized",
        "formal_field_registry_update_authorized",
        "writeback_request_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "runtime_topology_path_authorized",
        "runtime_path_enabled",
        "scheduler_route_authorized",
        "execution_handoff_authorized",
        "runtime_shadow_mode_authorized",
        "drl_execution_authorized",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    }

    assert set(non_authorizations) == expected_false_keys
    assert all(value is False for value in non_authorizations.values())


def test_fixture_cases_never_materialize_memory_records() -> None:
    fixture = load_json_dict(FIXTURE_PATH)
    cases = cast(list[JsonDict], fixture["fixture_cases"])

    assert {case["case_id"] for case in cases} == {
        "aem_write_candidate_preview_minimal_positive_fixture_v1",
        "aem_write_candidate_preview_negative_evidence_fixture_v1",
        "aem_write_candidate_preview_missing_receipt_fixture_v1",
    }

    for case in cases:
        assert case["scenario_kind"] == "non_executing_business_requirement_fixture"
        assert case["formal_write_request_created"] is False
        assert case["memory_write_authorized"] is False
        assert case["memory_record_created"] is False
        assert case["runtime_path_enabled"] is False
        output_summary = cast(JsonDict, case["output_summary"])
        assert output_summary["authority_source"] is False
        assert output_summary["persisted_memory_record"] is None


def test_denied_cases_are_fail_closed() -> None:
    fixture = load_json_dict(FIXTURE_PATH)
    denied_cases = cast(list[JsonDict], fixture["denied_cases"])

    assert {case["case_id"] for case in denied_cases} == {
        "missing_grant_decision_receipt_candidate_ref",
        "runtime_shadow_mode_requested",
        "formal_write_request_schema_promotion_requested",
        "persisted_memory_record_materialization_requested",
    }

    for case in denied_cases:
        assert case["expected_decision"] == "deny_fail_closed"
        for key, value in case.items():
            if key.endswith("_authorized") or key.endswith("_granted"):
                assert value is False


def test_upstream_candidate_references_are_not_authority_sources() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    upstream_refs = cast(list[JsonDict], manifest["upstream_candidate_references"])

    assert {ref["repo"] for ref in upstream_refs} == {"aiant-contracts", "aiant-core", "aiant-mmn"}
    for ref in upstream_refs:
        assert ref["authority_source"] is False

    authority_semantics = cast(JsonDict, manifest["authority_semantics"])
    assert authority_semantics["candidate_preview_is_authority_source"] is False
    assert authority_semantics["grant_decision_receipt_candidate_is_authority_source"] is False
    assert authority_semantics["business_requirement_fixture_is_runtime_shadow_mode"] is False
    assert authority_semantics["boolean_authority_fields_are_derived_summaries"] is True
    assert authority_semantics["fail_closed_default"] is True


def test_candidate_preview_contract_excludes_runtime_fields() -> None:
    fixture = load_json_dict(FIXTURE_PATH)
    contract = cast(JsonDict, fixture["candidate_preview_contract"])

    forbidden_fields = set(cast(list[str], contract["forbidden_runtime_fields"]))
    assert {
        "memory_record_id",
        "persisted_at",
        "writeback_commit_hash",
        "runtime_route_id",
        "scheduler_job_id",
        "execution_handoff_id",
        "shadow_mode_trace_id",
        "trading_signal_id",
    } <= forbidden_fields

    assert contract["materialized_memory_record_allowed"] is False
    assert contract["formal_write_request_allowed"] is False
