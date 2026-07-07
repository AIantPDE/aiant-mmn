from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "MMN_AEM_FIELD_SUGGESTION_MATURITY_BOUNDARY_V0.md"
)
MANIFEST_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "mmn_aem_field_suggestion_maturity_boundary_v0.json"
)
FIXTURE_PATH = ROOT / (
    "tests/fixtures/business_capabilities/mmn_authority_event_memory/"
    "aem_field_suggestion_maturity_boundary_v0.json"
)
SOURCE_CHECKPOINT_REF = "MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0"
SOURCE_DECISION_PLAN_REF = "MMN_AEM_CANDIDATE_FIELD_NEED_DECISION_LEDGER_PLAN_V0"
SENTINEL = "MMN_AEM_FIELD_SUGGESTION_MATURITY_BOUNDARY_V0_READY"


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


def test_maturity_boundary_sentinel_and_source_refs_are_present() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    assert SENTINEL in doc
    assert manifest["sentinel"] == SENTINEL
    assert fixture["sentinel"] == SENTINEL
    assert manifest["source_checkpoint_ref"] == SOURCE_CHECKPOINT_REF
    assert fixture["source_checkpoint_ref"] == SOURCE_CHECKPOINT_REF
    assert manifest["source_decision_plan_ref"] == SOURCE_DECISION_PLAN_REF
    assert fixture["source_decision_plan_ref"] == SOURCE_DECISION_PLAN_REF
    assert SOURCE_CHECKPOINT_REF in doc
    assert SOURCE_DECISION_PLAN_REF in doc


def test_corrected_chain_starts_from_provisional_inputs_not_mature_suggestions() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    corrected_chain = _as_list_of_str(manifest["corrected_chain"])
    assert corrected_chain[:4] == [
        "seed_scenario_derived_provisional_field_suggestion_inputs",
        "AEM_1_to_AEM_6_subcapability_pressure_reviews",
        "field_pressure_ledger_entries",
        "reviewed_candidate_field_suggestions",
    ]
    assert corrected_chain == _as_list_of_str(fixture["corrected_chain"])
    assert "seed-scenario-derived provisional field suggestion inputs" in doc
    assert "reviewed candidate field suggestions" in doc
    assert "provisional_field_suggestion_input" in doc
    assert "reviewed_candidate_field_suggestion" in doc


def test_previous_lane_status_is_plan_scaffold_not_completed_validation() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    status = _as_dict(manifest["previous_lane_status"])
    fixture_status = _as_dict(fixture["current_lane_status"])

    assert status == fixture_status
    assert status["field_pressure_ledger_review_checkpoint"] == (
        "scaffold_ready_not_completed_AEM_1_to_AEM_6_validation"
    )
    assert status["candidate_field_need_decision_ledger_plan"] == (
        "plan_ready_no_decision_records_created"
    )
    assert status["contracts_governance_review_handoff"] == "deferred"
    assert fixture["reviewed_candidate_field_suggestions_available"] is False
    assert fixture["candidate_need_decision_records_created"] is False
    assert fixture["aem_1_to_aem_6_pressure_reviews_required"] is True
    assert "candidate_field_need_decision_records_created = false" in doc


def test_unreviewed_provisional_inputs_are_not_reviewed_candidate_suggestions() -> None:
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    correction = _as_dict(manifest["maturity_correction"])
    provisional_inputs = _as_entry_list(fixture["provisional_inputs"])

    assert correction["loose_previous_term"] == "candidate_field_suggestion"
    assert correction["strict_split"] == [
        "provisional_field_suggestion_input",
        "reviewed_candidate_field_suggestion",
    ]
    assert correction["unreviewed_provisional_inputs_are_reviewed_candidate_suggestions"] is False
    assert (
        correction["reviewed_candidate_suggestions_require_aem_subcapability_pressure_review"]
        is True
    )
    assert provisional_inputs
    for entry in provisional_inputs:
        assert entry["is_reviewed_candidate_field_suggestion"] is False
        assert "required_review" in entry


def test_aem_1_to_aem_6_pressure_reviews_are_required_before_reviewed_suggestions() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    reviews = set(_as_list_of_str(manifest["required_subcapability_pressure_reviews"]))

    assert reviews == {
        "AEM_1_observed_signal_anchoring_pressure_review",
        "AEM_2_authority_source_retrieval_pressure_review",
        "AEM_3_attribution_hypothesis_pressure_review",
        "AEM_4_anti_bias_review_pressure_review",
        "AEM_5_memory_disposition_pressure_review",
        "AEM_6_future_reuse_boundary_pressure_review",
    }
    for review in reviews:
        assert review in doc


def test_minimum_review_questions_preserve_absence_test_and_witness_boundary() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    questions = set(_as_list_of_str(manifest["minimum_review_questions"]))

    assert "failure_if_missing_is_concrete" in questions
    assert "AEM_or_ORSC_target_is_affected" in questions
    assert "existing_field_substitution_is_not_safe_or_is_explicitly_selected" in questions
    assert "minimum_auditable_information_is_identified" in questions
    assert "evidence_receipt_witness_slots_are_separated" in questions
    assert "authority_envelope_witness_is_required_when_admissibility_is_claimed" in questions
    assert "failure_if_missing_is_concrete" in doc
    assert "evidence_receipt_witness_slots_are_separated" in doc


def test_forbidden_interpretations_block_shortcuts_and_misreadings() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    forbidden = set(_as_list_of_str(manifest["forbidden_interpretations"]))

    assert forbidden == set(_as_list_of_str(fixture["forbidden_interpretations"]))
    assert "unreviewed_provisional_input_to_reviewed_candidate_field_suggestion" in forbidden
    assert "seed_field_list_to_candidate_field_need" in forbidden
    assert (
        "candidate_need_decision_ledger_plan_to_candidate_need_decision_records_created"
        in forbidden
    )
    assert "gvr_intent_to_observed_signal_ref" in forbidden
    assert "gvr_intent_to_attribution_link_ref" in forbidden
    assert "ordinary_evidence_to_orsc_witness" in forbidden
    assert "receipt_to_orsc_witness" in forbidden
    assert "authority_boolean_to_authority_source" in forbidden
    assert "GVR Intent -> observed_signal_ref" in doc
    assert "ordinary evidence -> ORSC witness" in doc


def test_theory_boundaries_keep_gvr_intent_and_orsc_witness_separate() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    boundary = _as_dict(manifest["theory_boundaries"])
    fixture_boundary = _as_dict(fixture["theory_boundary_assertions"])

    assert boundary == fixture_boundary
    assert boundary["gvr_display_may_enter_observed_signal_anchoring"] is True
    assert boundary["gvr_possess_intent_remain_inference_candidates_only"] is True
    assert boundary["intent_attribution_candidate_ref"] == (
        "attribution_hypothesis_pressure_source_ref"
    )
    assert boundary["intent_attribution_candidate_is_attribution_link_ref"] is False
    assert boundary["orsc_witness"] == "authority_envelope"
    assert boundary["authority_booleans"] == "derived_summaries_only"
    assert "ORSC witness = authority envelope" in doc
    assert "Authority booleans are derived summaries only" in doc


def test_denied_scope_keeps_formal_runtime_memory_drl_and_trading_closed() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    denied = _as_dict(manifest["denied_scope"])

    assert denied == _as_dict(fixture["denied_scope"])
    assert denied["formal_field_registry_update"] is False
    assert denied["contracts_schema_created"] is False
    assert denied["scanner_implemented"] is False
    assert denied["runtime_activation"] == "denied"
    assert denied["memory_write"] == "denied"
    assert denied["drl_execution_authorized"] is False
    assert denied["trading_signal_authorized"] is False
    assert denied["candidate_need_decision_records_created"] is False
    assert denied["contracts_governance_handoff_started"] is False
    assert denied["non_executing"] is True
    assert denied["non_authorizing"] is True
    assert denied["candidate_only"] is True
    assert "formal_field_registry_update = false" in doc
    assert "runtime_activation = denied" in doc


def test_next_selected_delta_is_aem1_specific_not_contracts_governance_handoff() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    expected_next = "mmn: add AEM-1 observed signal anchoring pressure review v0"

    assert manifest["next_selected_delta"] == expected_next
    assert fixture["next_selected_delta"] == expected_next
    assert "AEM-wide contracts/governance handoff = deferred" in doc
    assert expected_next in doc
