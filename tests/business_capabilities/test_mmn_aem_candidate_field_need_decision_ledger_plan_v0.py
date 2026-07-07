from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0.md"
)
MANIFEST_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "mmn_aem_candidate_field_need_decision_ledger_plan_v0.json"
)
FIXTURE_PATH = ROOT / (
    "tests/fixtures/business_capabilities/mmn_authority_event_memory/"
    "aem_candidate_field_need_decision_ledger_plan_v0.json"
)
SOURCE_PLAN_REF = "MMN_AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0"
SOURCE_CHECKPOINT_REF = "MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0"
SOURCE_CHECKPOINT_SENTINEL = "MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0_READY"
SENTINEL = "MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0_READY"


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _as_dict(value: Any) -> dict[str, Any]:
    assert isinstance(value, dict)
    return cast(dict[str, Any], value)


def _as_list_of_str(value: Any) -> list[str]:
    assert isinstance(value, list)
    for item in value:
        assert isinstance(item, str)
    return value


def _as_entry_list(value: Any) -> list[dict[str, Any]]:
    assert isinstance(value, list)
    entries: list[dict[str, Any]] = []
    for item in value:
        assert isinstance(item, dict)
        entries.append(cast(dict[str, Any], item))
    return entries


def test_plan_sentinel_and_predecessor_checkpoint_are_present() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    assert SENTINEL in doc
    assert manifest["sentinel"] == SENTINEL
    assert fixture["sentinel"] == SENTINEL
    assert manifest["source_plan_ref"] == SOURCE_PLAN_REF
    assert fixture["source_plan_ref"] == SOURCE_PLAN_REF
    assert manifest["source_checkpoint_ref"] == SOURCE_CHECKPOINT_REF
    assert fixture["source_checkpoint_ref"] == SOURCE_CHECKPOINT_REF
    assert manifest["source_checkpoint_sentinel"] == SOURCE_CHECKPOINT_SENTINEL
    assert fixture["source_checkpoint_sentinel"] == SOURCE_CHECKPOINT_SENTINEL
    assert SOURCE_CHECKPOINT_REF in doc
    assert SOURCE_PLAN_REF in doc


def test_decision_chain_keeps_candidate_need_outside_formal_surfaces() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    denied_scope = _as_dict(manifest["denied_scope"])

    decision_chain = _as_list_of_str(manifest["decision_chain"])
    assert decision_chain[:3] == [
        "candidate_field_suggestion",
        "field_pressure_ledger_review_checkpoint",
        "candidate_field_need_decision_ledger_plan",
    ]
    assert "later_contracts_governance_review" in decision_chain
    assert "possible_formal_registry_proposal_later" == decision_chain[-1]

    assert denied_scope["formal_field_registry_update"] is False
    assert denied_scope["contracts_schema_created"] is False
    assert denied_scope["scanner_implemented"] is False
    assert denied_scope["runtime_activation"] == "denied"
    assert denied_scope["memory_write"] == "denied"
    assert denied_scope["candidate_need_decisions_default_to_formal_fields"] is False
    assert fixture["candidate_need_decision_ledger_is_formal_registry"] is False
    assert fixture["candidate_need_decision_ledger_is_contract_schema"] is False
    assert "formal_field_registry_update = false" in doc
    assert "candidate_need_decisions_default_to_formal_fields = false" in doc


def test_all_decision_outcomes_are_documented_and_represented() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    entries = _as_entry_list(fixture["decision_rows"])

    expected_outcomes = {
        "candidate_need_ready_for_later_contracts_governance_review",
        "defer_need_until_more_recurrence",
        "defer_need_due_to_naming_or_grouping_ambiguity",
        "defer_need_due_to_existing_field_substitution_review",
        "reject_need_due_to_no_concrete_failure_if_missing",
        "reject_need_due_to_authority_or_runtime_risk",
        "route_to_contracts_governance_review_without_need_promotion",
    }
    assert set(_as_list_of_str(manifest["decision_outcomes"])) == expected_outcomes
    assert set(_as_list_of_str(fixture["decision_outcomes"])) == expected_outcomes
    assert {entry["decision_outcome"] for entry in entries} == expected_outcomes
    for outcome in expected_outcomes:
        assert outcome in doc


def test_minimum_decision_rows_are_non_authorizing() -> None:
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    minimum_fields = set(_as_list_of_str(manifest["minimum_decision_entry_fields"]))
    entries = _as_entry_list(fixture["decision_rows"])

    assert entries
    for entry in entries:
        assert minimum_fields <= set(entry)
        assert entry["source_checkpoint_ref"] == SOURCE_CHECKPOINT_REF
        assert entry["non_authorizing_boundary"] is True
        assert isinstance(entry["required_evidence_refs"], list)
        assert isinstance(entry["required_receipt_refs"], list)
        assert isinstance(entry["required_authority_envelope_refs"], list)
        must_not_authorize = _as_list_of_str(entry["must_not_authorize"])
        assert must_not_authorize
        assert not entry["decision_outcome"].endswith("formal_registry_update")


def test_aem3_intent_attribution_candidate_stays_pressure_source_not_link() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    aem3 = _as_dict(manifest["aem3_boundary"])
    assert aem3["correct_pressure_source_ref"] == ("attribution_hypothesis_pressure_source_ref")
    assert aem3["direct_intent_to_attribution_link_ref_allowed"] is False
    assert aem3["direct_intent_to_memory_record_allowed"] is False
    assert aem3["direct_intent_to_runtime_activation_claim_allowed"] is False

    entries = _as_entry_list(fixture["decision_rows"])
    pressure_source_entry = next(
        entry
        for entry in entries
        if entry["candidate_field_suggestion"] == "attribution_hypothesis_pressure_source_ref"
    )
    assert pressure_source_entry["decision_outcome"] == (
        "candidate_need_ready_for_later_contracts_governance_review"
    )
    assert "Intent remains inference candidate" in pressure_source_entry["gvr_layer_boundary"]
    assert "attribution_link_ref" in pressure_source_entry["must_not_authorize"]

    forbidden_shortcut = next(
        entry
        for entry in entries
        if entry["candidate_field_suggestion"] == "gvr_intent_to_attribution_link_ref"
    )
    assert forbidden_shortcut["decision_outcome"] == (
        "reject_need_due_to_authority_or_runtime_risk"
    )
    assert "GVR Intent -> attribution_link_ref" in doc
    assert "not attribution_link_ref" in doc


def test_orsc_witness_and_authority_booleans_keep_envelope_boundary() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    orsc = _as_dict(manifest["orsc_semantics"])
    assert orsc["evidence"] == "ordinary_evidence_material"
    assert orsc["receipt"] == "traceable_step_receipt"
    assert orsc["witness"] == "authority_envelope"
    assert orsc["authority_booleans"] == "derived_summaries_only"

    boundaries = _as_dict(fixture["theory_boundary_assertions"])
    assert boundaries["orsc_witness_semantics"] == "authority_envelope_only"
    assert boundaries["boolean_authority_fields_are_derived_summaries_only"] is True

    entries = _as_entry_list(fixture["decision_rows"])
    authority_entry = next(
        entry
        for entry in entries
        if entry["candidate_field_suggestion"] == "authority_envelope_ref"
    )
    assert authority_entry["orsc_slot"] == "witness"
    assert authority_entry["required_authority_envelope_refs"] == ["authority_envelope_ref"]
    assert "witness = authority envelope" in doc
    assert "derived summary" in doc


def test_denied_runtime_memory_and_drl_surfaces_remain_closed() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    denied_scope = _as_dict(manifest["denied_scope"])

    assert denied_scope["runtime_authorizing"] is False
    assert denied_scope["memory_record_creation_authorized"] is False
    assert denied_scope["drl_execution_authorized"] is False
    assert denied_scope["trading_signal_authorized"] is False
    assert denied_scope["candidate_need_decision_ledger_is_authority_source"] is False
    assert fixture["candidate_need_decision_ledger_authorizes_runtime"] is False
    assert fixture["candidate_need_decision_ledger_authorizes_memory_write"] is False

    assert "drl_execution_authorized = false" in doc
    assert "trading_signal_authorized = false" in doc
    assert "runtime_activation = denied" in doc
    assert "memory_write = denied" in doc
