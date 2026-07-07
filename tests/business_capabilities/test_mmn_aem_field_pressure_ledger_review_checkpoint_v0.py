from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0.md"
)
MANIFEST_PATH = ROOT / (
    "docs/business_capabilities/mmn_authority_event_memory/"
    "mmn_aem_field_pressure_ledger_review_checkpoint_v0.json"
)
FIXTURE_PATH = ROOT / (
    "tests/fixtures/business_capabilities/mmn_authority_event_memory/"
    "aem_field_pressure_ledger_review_checkpoint_v0.json"
)
SOURCE_PLAN_REF = "MMN_AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0"
SENTINEL = "MMN_AEM_FIELD_PRESSURE_LEDGER_REVIEW_CHECKPOINT_V0_READY"


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _as_list_of_str(value: Any) -> list[str]:
    assert isinstance(value, list)
    for item in value:
        assert isinstance(item, str)
    return value


def _as_dict(value: Any) -> dict[str, Any]:
    assert isinstance(value, dict)
    return cast(dict[str, Any], value)


def _as_entry_list(value: Any) -> list[dict[str, Any]]:
    assert isinstance(value, list)
    entries: list[dict[str, Any]] = []
    for item in value:
        assert isinstance(item, dict)
        entries.append(cast(dict[str, Any], item))
    return entries


def test_checkpoint_sentinel_and_source_plan_are_present() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    assert SENTINEL in doc
    assert manifest["sentinel"] == SENTINEL
    assert fixture["sentinel"] == SENTINEL
    assert manifest["source_plan_ref"] == SOURCE_PLAN_REF
    assert fixture["source_plan_ref"] == SOURCE_PLAN_REF
    assert SOURCE_PLAN_REF in doc


def test_all_review_dispositions_and_pressure_strengths_are_documented() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    expected_dispositions = {
        "ready_for_candidate_need_review",
        "defer_until_more_recurrence",
        "defer_due_to_naming_ambiguity",
        "defer_due_to_existing_field_substitution",
        "reject_due_to_no_concrete_failure_if_missing",
        "reject_due_to_authority_or_runtime_risk",
        "needs_contracts_governance_review_later",
    }
    assert set(_as_list_of_str(manifest["review_dispositions"])) == expected_dispositions
    assert set(_as_list_of_str(fixture["review_dispositions"])) == expected_dispositions
    for disposition in expected_dispositions:
        assert disposition in doc

    expected_strengths = {
        "P0 no pressure",
        "P1 descriptive pressure",
        "P2 review pressure",
        "P3 gate pressure",
        "P4 safety / authority pressure",
    }
    assert set(_as_list_of_str(manifest["pressure_strength_scale"])) == expected_strengths
    assert set(_as_list_of_str(fixture["pressure_strength_scale"])) == expected_strengths
    for strength in expected_strengths:
        assert strength in doc


def test_candidate_field_suggestions_are_not_candidate_needs_by_default() -> None:
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    denied_scope = _as_dict(manifest["denied_scope"])

    assert denied_scope["candidate_field_suggestions_default_to_candidate_needs"] is False
    assert fixture["candidate_field_suggestions_default_to_candidate_needs"] is False
    assert manifest["status"] == "candidate_review_checkpoint"

    review_chain = _as_list_of_str(manifest["review_chain"])
    assert review_chain[0] == "candidate_field_suggestion"
    assert review_chain[1] == "field_pressure_ledger_review"
    assert "candidate_field_need" in review_chain[2]


def test_denied_surfaces_keep_registry_contracts_scanner_runtime_memory_closed() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    denied_scope = _as_dict(manifest["denied_scope"])

    assert denied_scope["formal_field_registry_update"] is False
    assert denied_scope["contracts_schema_created"] is False
    assert denied_scope["scanner_implemented"] is False
    assert denied_scope["runtime_activation"] == "denied"
    assert denied_scope["memory_write"] == "denied"
    assert denied_scope["runtime_authorizing"] is False

    assert fixture["formal_field_registry_updated"] is False
    assert fixture["contracts_schema_created"] is False
    assert fixture["scanner_implemented"] is False
    assert fixture["runtime_activation"] == "denied"
    assert fixture["memory_write"] == "denied"

    assert "formal_field_registry_update = false" in doc
    assert "contracts_schema_created = false" in doc
    assert "runtime_activation = denied" in doc
    assert "memory_write = denied" in doc


def test_aem3_attribution_candidate_uses_pressure_source_not_link_ref() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    boundary = _as_dict(manifest["aem3_boundary"])
    must_not = set(_as_list_of_str(boundary["must_not_directly_be"]))
    assert boundary["intent_or_attribution_candidate_ref"] == (
        "attribution_hypothesis_pressure_source_ref"
    )
    assert boundary["direct_gvr_intent_to_attribution_link_ref_allowed"] is False
    assert "attribution_link_ref" in must_not
    assert "attribution_link_receipt_ref" in must_not
    assert "memory_record" in must_not
    assert "runtime_activation_claim" in must_not

    boundary_case = _as_dict(fixture["aem3_boundary_case"])
    assert boundary_case["correct_pressure_source_ref"] == (
        "attribution_hypothesis_pressure_source_ref"
    )
    assert boundary_case["direct_attribution_link_ref_allowed"] is False
    assert "Intent / Attribution Candidate" in boundary_case["input_candidate"]

    assert "Intent / Attribution Candidate" in doc
    assert "-> attribution_hypothesis_pressure_source_ref" in doc
    assert "!= attribution_link_ref" in doc


def test_gvr_and_orsc_witness_boundaries_are_authority_safe() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)

    assertions = _as_dict(manifest["theory_boundary_assertions"])
    assert assertions["gvr_display_may_enter_observed_signal_anchoring"] is True
    assert assertions["gvr_possess_intent_remain_inference_candidates_only"] is True
    assert assertions["gvr_is_semantic_front_end_not_aem_replacement"] is True
    assert assertions["cagp_reviews_scenario_driven_pressure_only"] is True
    assert assertions["orsc_witness_semantics"] == "authority_envelope_only"

    orsc = _as_dict(fixture["orsc_semantics"])
    assert orsc["evidence"] == "ordinary_evidence_material"
    assert orsc["receipt"] == "traceable_step_receipt"
    assert orsc["witness"] == "authority_envelope"

    assert "GVR Display may enter observed signal anchoring" in doc
    assert "GVR Possess / Intent remain inference candidates only" in doc
    assert "witness = authority envelope" in doc


def test_ledger_entries_have_minimum_fields_and_substitution_review() -> None:
    manifest = _read_json(MANIFEST_PATH)
    fixture = _read_json(FIXTURE_PATH)
    minimum_fields = set(_as_list_of_str(manifest["minimum_ledger_entry_fields"]))
    entries = _as_entry_list(fixture["ledger_entries"])

    assert entries
    for entry in entries:
        assert minimum_fields <= set(entry)
        assert entry["source_plan_ref"] == SOURCE_PLAN_REF
        assert entry["non_authorizing_boundary"] is True
        assert isinstance(entry["existing_field_substitution_review"], dict)
        assert str(entry["pressure_strength"]).startswith("P")

    aem3_entries = [
        entry
        for entry in entries
        if entry["aem_sub_capability"] == "AEM-3 attribution chain construction"
    ]
    assert aem3_entries
    assert any(
        entry["candidate_field_suggestion"] == "attribution_hypothesis_pressure_source_ref"
        for entry in aem3_entries
    )
    for entry in aem3_entries:
        assert entry["review_disposition"] in {
            "ready_for_candidate_need_review",
            "needs_contracts_governance_review_later",
        }
