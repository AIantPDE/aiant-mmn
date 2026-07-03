from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
DOC_FILENAME = (
    "MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_CAPABILITY_SCENARIO_TAXONOMY"
    "_AND_FIELD_REGISTRY_FEEDBACK_BOUNDARY_V0.md"
)
MANIFEST_FILENAME = (
    "mmn_authority_event_memory_business_capability_scenario_taxonomy"
    "_and_field_registry_feedback_boundary_v0.json"
)
FIXTURE_FILENAME = (
    "business_capability_scenario_taxonomy_and_field_registry_feedback_boundary_v0.json"
)

DOC_PATH = ROOT / "docs" / "verification" / DOC_FILENAME
MANIFEST_PATH = ROOT / "docs" / "verification" / MANIFEST_FILENAME
FIXTURE_PATH = ROOT / "tests" / "fixtures" / "mmn_authority_event_memory" / FIXTURE_FILENAME

JsonDict = dict[str, Any]


def load_json_dict(path: Path) -> JsonDict:
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    return data


def test_business_capability_taxonomy_assets_exist() -> None:
    assert DOC_PATH.exists()
    assert MANIFEST_PATH.exists()
    assert FIXTURE_PATH.exists()


def test_business_capability_taxonomy_doc_centers_aem_six_capabilities() -> None:
    doc = DOC_PATH.read_text(encoding="utf-8")

    required_markers = [
        "MMN_AUTHORITY_EVENT_MEMORY_BUSINESS_REQUIREMENT_SCENARIO_FIXTURES_V0",
        "AEM 的业务能力至少包含六个子能力",
        "拐点识别能力",
        "权威事件检索能力",
        "归因链构造能力",
        "反偏差能力",
        "记忆晋级能力",
        "未来复用能力",
        "memory construction for future reasoning",
        "field registry feedback 不是 AEM business capability 的起点",
        "CAGP V1.1 可以作为背景关系存在，但不是本 PR 的主要修正依据",
        "ready_for_scanner_implementation_skeleton: false",
        "AEM_BUSINESS_CAPABILITY_SCENARIO_TAXONOMY_FIELD_REGISTRY_FEEDBACK_BOUNDARY_V0_READY",
    ]

    for marker in required_markers:
        assert marker in doc


def test_business_capability_taxonomy_manifest_matches_fixture() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    fixture = load_json_dict(FIXTURE_PATH)

    comparable_keys = [
        "asset_id",
        "asset_kind",
        "fixture_family_version",
        "plan_status",
        "correction_focus",
        "source_document_under_review",
        "sentinel",
        "primary_correction",
        "legacy_v0_diagnosis",
        "aem_six_subcapabilities",
        "taxonomy_reclassification",
        "required_next_step",
        "deferred_steps",
        "promotion_gates",
        "boundary",
    ]

    for key in comparable_keys:
        assert fixture[key] == manifest[key]


def test_primary_correction_is_not_cagp_v1_1_first() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    correction = manifest["primary_correction"]

    assert correction["wrong_focus_to_avoid"] == (
        "using_CAGP_V1_1_paper_as_the_primary_driver_for_this_MMN_pr"
    )
    assert correction["correct_focus"] == (
        "redefine_AEM_business_capability_by_six_subcapabilities_before_field_registry_feedback"
    )
    assert correction["cagp_role_in_this_pr"] == (
        "background_context_only_not_the_governing_source"
    )


def test_aem_six_subcapabilities_are_complete_and_ordered() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    capabilities = manifest["aem_six_subcapabilities"]

    capability_ids = [item["id"] for item in capabilities]
    assert capability_ids == [
        "turning_point_detection_capability",
        "authority_event_retrieval_capability",
        "attribution_link_construction_capability",
        "anti_bias_review_capability",
        "memory_promotion_capability",
        "future_reuse_capability",
    ]

    for item in capabilities:
        assert item["not_field_first"] is True
        assert item["cn"]
        assert item["question"]


def test_legacy_v0_is_reclassified_but_preserved() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    diagnosis = manifest["legacy_v0_diagnosis"]

    assert diagnosis["semantic_error"] == (
        "the_legacy_business_requirement_scenario_name_is_too_broad"
    )
    assert "field_registry_feedback" in diagnosis["actual_coverage"]
    assert "negative_boundary" in diagnosis["actual_coverage"]
    assert "complete_AEM_business_capability_scenario_suite" in (diagnosis["not_actual_coverage"])
    assert diagnosis["handling"] == (
        "keep_legacy_file_do_not_rename_this_pr_but_reclassify_it_downstream"
    )


def test_field_registry_feedback_is_downstream_of_six_capabilities() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    taxonomy = manifest["taxonomy_reclassification"]

    assert taxonomy["Layer_4_5a"] == (
        "AEM_six_subcapability_seed_scenarios_required_before_scanner_skeleton"
    )
    assert taxonomy["Layer_4_5b"] == (
        "field_registry_feedback_scenarios_downstream_of_six_subcapabilities"
    )
    assert taxonomy["Layer_4_5c"] == ("negative_boundary_and_forbidden_interpretation_scenarios")
    assert taxonomy["Layer_4_5d"] == ("non_executing_preview_and_scanner_planning_only_after_4_5a")


def test_next_step_is_aem_authority_source_seed_scenarios() -> None:
    manifest = load_json_dict(MANIFEST_PATH)

    assert manifest["required_next_step"] == (
        "mmn_draft_AEM_authority_source_event_memory_construction_seed_scenarios_v0"
    )
    assert (
        "governance_scanner_implementation_skeleton_after_AEM_six_subcapability_seed_suite"
        in (manifest["deferred_steps"])
    )


def test_business_capability_taxonomy_blocks_scanner_skeleton_readiness() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    gates = manifest["promotion_gates"]

    assert gates["ready_for_scanner_implementation_skeleton"] is False
    assert gates["ready_for_runtime_scanner"] is False
    assert gates["ready_for_memory_write"] is False
    assert gates["ready_for_formal_field_registry_update"] is False
    assert gates["ready_for_accepted_schema_surface_expansion"] is False


def test_business_capability_taxonomy_boundary_remains_non_authorizing() -> None:
    manifest = load_json_dict(MANIFEST_PATH)
    boundary = manifest["boundary"]

    assert boundary["candidate_only"] is True
    assert boundary["clarification_only"] is True
    assert boundary["non_authorizing"] is True
    assert boundary["non_executing"] is True
    assert boundary["docs_fixtures_tests_only"] is True

    denied_flags = [
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "writeback_request_authorized",
        "runtime_topology_path_authorized",
        "scheduler_route_authorized",
        "execution_handoff_authorized",
        "runtime_shadow_mode_authorized",
        "scanner_runtime_invocation_authorized",
        "formal_field_registry_update_authorized",
        "accepted_schema_surface_expansion_authorized",
        "drl_execution_authorized",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    ]

    for flag in denied_flags:
        assert boundary[flag] is False
