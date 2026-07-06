from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_FILENAME = "MMN_AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0.md"
MANIFEST_FILENAME = "mmn_aem_authority_source_seed_scenario_field_derivation_feedback_plan_v0.json"
FIXTURE_FILENAME = "authority_source_seed_scenario_field_derivation_feedback_plan_v0.json"

DOC_PATH = ROOT / "docs" / "business_capabilities" / "mmn_authority_event_memory" / DOC_FILENAME
MANIFEST_PATH = (
    ROOT / "docs" / "business_capabilities" / "mmn_authority_event_memory" / MANIFEST_FILENAME
)
FIXTURE_PATH = (
    ROOT
    / "tests"
    / "fixtures"
    / "business_capabilities"
    / "mmn_authority_event_memory"
    / FIXTURE_FILENAME
)


def _load_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def test_field_derivation_feedback_plan_files_exist() -> None:
    assert DOC_PATH.exists()
    assert MANIFEST_PATH.exists()
    assert FIXTURE_PATH.exists()


def test_doc_contains_cagp_v3_and_gvr_semantic_front_end_markers() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    required_markers = {
        "AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0_READY",
        "CAGP V3 alignment",
        "GVR semantic front-end for AEM",
        "Display-level semantic front-end",
        "Possess / Intent",
        "display_to_intent_to_attribution_without_anchor",
        "field pressure ledger",
        "absence test",
        "candidate field suggestion",
        "not yet candidate field need",
        "authority-envelope witness",
        "formal field registry",
        "memory_write_authority_granted = false",
        "runtime_topology_path_authorized = false",
        "drl_execution_authorized = false",
        "trading_signal_authorized = false",
        "future_live_execution_authorized = false",
    }

    for marker in required_markers:
        assert marker in text


def test_manifest_has_cagp_v3_alignment_and_gvr_front_end_policy() -> None:
    manifest = _load_json(MANIFEST_PATH)

    assert manifest["repo"] == "aiant-mmn"
    assert manifest["version"] == "v0_cagp_v3_semantic_front_end_alignment"
    assert manifest["formal_registry_update"] is False
    assert manifest["memory_write_authority_granted"] is False
    assert manifest["runtime_topology_path_authorized"] is False
    assert manifest["drl_execution_authorized"] is False
    assert manifest["trading_signal_authorized"] is False
    assert manifest["future_live_execution_authorized"] is False

    alignment = manifest["cagp_v3_alignment"]
    assert (
        "gvr_display_level_semantic_front_end_when_natural_language"
        in alignment["field_emergence_chain"]
    )
    assert "candidate_field_suggestion" in alignment["field_emergence_chain"]
    assert "designer_enum_to_candidate_field_need" in alignment["reverse_path_denied"]
    assert "display_to_intent_to_attribution_without_anchor" in alignment["reverse_path_denied"]

    gvr = manifest["gvr_semantic_front_end"]
    assert gvr["display"].startswith("observable")
    assert "inference proposal only" in gvr["possess"]
    assert "inference proposal only" in gvr["intent"]
    assert "gvr_display_level_semantic_front_end" in gvr["allowed_chain"]
    assert "intent_inference_to_attribution_conclusion" in gvr["prohibited_shortcuts"]


def test_field_pressure_policy_targets_remain_non_registry_targets() -> None:
    manifest = _load_json(MANIFEST_PATH)
    pressure_policy = manifest["field_pressure_policy"]

    assert "absence_test" in pressure_policy
    assert "P4" in pressure_policy["pressure_strength_scale"]
    assert "authority_envelope_witness" in pressure_policy["target_objects"]
    assert "formal_field_registry" not in pressure_policy["target_objects"]


def test_each_sub_capability_has_pressure_observations_projection_and_suggestions() -> None:
    manifest = _load_json(MANIFEST_PATH)

    derivations = manifest["aem_sub_capability_field_derivations"]
    assert len(derivations) == 6
    assert {item["id"] for item in derivations} == {
        "AEM-1",
        "AEM-2",
        "AEM-3",
        "AEM-4",
        "AEM-5",
        "AEM-6",
    }

    for item in derivations:
        projection = item["orsc_projection"]
        assert set(projection) == {
            "residual",
            "ordered_next_step",
            "evidence_gate",
            "evidence",
            "receipt",
            "witness",
        }
        assert projection["evidence"] in item["candidate_field_suggestions"]
        assert projection["receipt"] in item["candidate_field_suggestions"]
        assert projection["witness"] in item["candidate_field_suggestions"]
        assert projection["witness"].endswith("_authority_envelope_ref")
        assert item["field_pressure_observations"]
        assert len(item["candidate_field_suggestions"]) >= 6
        assert item["candidate_need_status"] == (
            "not_yet_candidate_field_need_until_pressure_review"
        )


def test_candidate_field_suggestion_index_is_forward_derived() -> None:
    manifest = _load_json(MANIFEST_PATH)
    derivations = manifest["aem_sub_capability_field_derivations"]
    index = manifest["candidate_field_suggestion_index"]

    expected_pairs = {
        (field, item["id"]) for item in derivations for field in item["candidate_field_suggestions"]
    }
    indexed_pairs = {(item["field_name"], item["derived_from_sub_capability"]) for item in index}

    assert indexed_pairs == expected_pairs
    assert all(item["seed_scenario_ref"] for item in index)
    assert all(item["pressure_target"] for item in index)
    assert all(
        item["promotion_note"]
        == (
            "field pressure must be reviewed before candidate field need "
            "and later contracts/governance review"
        )
        for item in index
    )


def test_natural_language_signal_policy_keeps_gvr_and_llm_non_authoritative() -> None:
    manifest = _load_json(MANIFEST_PATH)
    policy = manifest["natural_language_observed_signal_policy"]

    assert "raw_text_preservation" in policy["required_layers"]
    assert "source_span_anchor" in policy["required_layers"]
    assert "detection_receipt" in policy["required_layers"]
    assert "authority_envelope_witness" in policy["required_layers"]
    assert "Display-level semantic front-end" in policy["semantic_front_end"]
    assert "not an observed signal" in policy["possess_policy"]
    assert "not attribution" in policy["intent_policy"]
    assert "not an authority source" in policy["llm_policy"]


def test_fixture_mirrors_v3_front_end_boundary_and_sentinel() -> None:
    fixture = _load_json(FIXTURE_PATH)

    assert "cagp_v3_alignment" in fixture
    assert "gvr_semantic_front_end" in fixture
    assert fixture["gvr_semantic_front_end"]["display"].startswith("observable")

    boundary = fixture["non_authorizing_boundary"]
    assert boundary["memory_write_authority_granted"] is False
    assert boundary["runtime_topology_path_authorized"] is False
    assert boundary["drl_execution_authorized"] is False
    assert boundary["trading_signal_authorized"] is False
    assert boundary["future_live_execution_authorized"] is False
    assert fixture["sentinel"] == (
        "AEM_AUTHORITY_SOURCE_SEED_SCENARIO_FIELD_DERIVATION_FEEDBACK_PLAN_V0_READY"
    )
