from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_FILENAME = "MMN_AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0.md"
MANIFEST_FILENAME = "mmn_aem_authority_source_event_memory_construction_seed_scenarios_v0.json"
FIXTURE_FILENAME = "authority_source_event_memory_construction_seed_scenarios_v0.json"

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


JsonObject = dict[str, Any]


def _load_json(path: Path) -> JsonObject:
    return cast(JsonObject, json.loads(path.read_text(encoding="utf-8")))


def test_aem_seed_scenarios_doc_contains_core_markers() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    required_markers = {
        "AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0_READY",
        "AEM 六个子业务能力",
        "拐点识别能力",
        "权威事件检索能力",
        "归因链构造能力",
        "反偏差能力",
        "记忆晋级能力",
        "未来复用能力",
        "ORSC V10 实施方法",
        "Observe residual",
        "Evidence-gated admissibility",
        "Authority decision evidence envelope as witness",
        "candidate field registry",
        "formal field registry",
        "runtime activation",
    }

    missing = {marker for marker in required_markers if marker not in text}
    assert not missing


def test_aem_seed_scenarios_manifest_shape() -> None:
    manifest = _load_json(MANIFEST_PATH)

    assert manifest["object_name"] == (
        "MMN_AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0"
    )
    assert manifest["version"] == "v0"
    assert manifest["repo"] == "aiant-mmn"
    assert manifest["status"] == "draft"
    assert manifest["sentinel"] == (
        "AEM_AUTHORITY_SOURCE_EVENT_MEMORY_CONSTRUCTION_SEED_SCENARIOS_V0_READY"
    )

    modes = set(manifest["mode"])
    assert "candidate_only" in modes
    assert "seed_scenario_only" in modes
    assert "non_executing" in modes
    assert "non_authorizing" in modes

    subcaps = manifest["aem_business_subcapabilities"]
    assert len(subcaps) == 6
    assert {item["name_cn"] for item in subcaps} == {
        "拐点识别能力",
        "权威事件检索能力",
        "归因链构造能力",
        "反偏差能力",
        "记忆晋级能力",
        "未来复用能力",
    }


def test_aem_seed_scenarios_cover_each_subcapability() -> None:
    manifest = _load_json(MANIFEST_PATH)

    subcap_ids = {item["id"] for item in manifest["aem_business_subcapabilities"]}
    scenario_subcaps = {item["primary_subcapability"] for item in manifest["seed_scenarios"]}

    assert len(manifest["seed_scenarios"]) == 6
    assert scenario_subcaps == subcap_ids


def test_aem_seed_scenarios_use_orsc_v10_method() -> None:
    manifest = _load_json(MANIFEST_PATH)
    method = manifest["orsc_v10_implementation_method"]

    assert method["not_runtime"] is True
    keywords = set(method["keywords"])
    assert "evidence-gated action admissibility" in keywords
    assert "receipt-sealed action admissibility" in keywords
    assert "authority decision evidence envelope as ORSC witness" in keywords
    assert "scope-bound authority admissibility" in keywords

    required_orsc_keys = {
        "residual",
        "ordered_next_step",
        "evidence_gate",
        "receipt",
        "witness",
    }
    for scenario in manifest["seed_scenarios"]:
        assert set(scenario["orsc_v10_application"]) == required_orsc_keys


def test_aem_seed_scenarios_derive_fields_from_scenarios() -> None:
    manifest = _load_json(MANIFEST_PATH)

    for scenario in manifest["seed_scenarios"]:
        assert scenario["real_world_shape"]
        assert len(scenario["field_derivation_steps"]) >= 3
        assert len(scenario["derived_field_candidates"]) >= 5
        assert scenario["boundary"]

    groups = manifest["derived_field_candidate_groups"]
    assert "signal_and_turning_point" in groups
    assert "authority_source_and_as_of" in groups
    assert "attribution_and_revision" in groups
    assert "anti_bias_and_scoring" in groups
    assert "promotion_decision" in groups
    assert "future_reuse_boundary" in groups


def test_aem_seed_scenarios_keep_non_authorizing_boundary() -> None:
    manifest = _load_json(MANIFEST_PATH)
    flags = manifest["explicit_non_authorizing_flags"]

    expected_false_flags = {
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "writeback_request_authorized",
        "runtime_topology_path_authorized",
        "scheduler_route_authorized",
        "execution_handoff_authorized",
        "runtime_shadow_mode_authorized",
        "drl_execution_authorized",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    }

    assert set(flags) == expected_false_flags
    assert all(value is False for value in flags.values())

    blocked = set(manifest["blocked_use"])
    assert "formal FIELD_REGISTRY update" in blocked
    assert "memory write" in blocked
    assert "scanner implementation" in blocked
    assert "runtime topology path" in blocked
    assert "DRL execution" in blocked
    assert "trading signal" in blocked
    assert "future live execution" in blocked


def test_aem_seed_scenarios_fixture_mirrors_manifest() -> None:
    manifest = _load_json(MANIFEST_PATH)
    fixture = _load_json(FIXTURE_PATH)

    assert fixture["fixture_name"] == (
        "authority_source_event_memory_construction_seed_scenarios_v0"
    )
    assert fixture["fixture_kind"] == "aem_native_seed_scenario_fixture"
    assert fixture["object_name"] == manifest["object_name"]
    assert fixture["sentinel"] == manifest["sentinel"]
    assert fixture["seed_scenarios"] == manifest["seed_scenarios"]
    assert fixture["explicit_non_authorizing_flags"] == (manifest["explicit_non_authorizing_flags"])
