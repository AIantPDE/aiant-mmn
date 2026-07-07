from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = (
    ROOT / "docs" / "terminology" / ("AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0.md")
)
MANIFEST_PATH = (
    ROOT / "docs" / "terminology" / ("aiant_linkage_family_cross_repo_adoption_checklist_v0.json")
)


def _read_doc() -> str:
    return DOC_PATH.read_text(encoding="utf-8")


def _read_manifest() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(MANIFEST_PATH.read_text(encoding="utf-8")))


def test_cross_repo_adoption_checklist_sentinel_and_boundary() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    assert "AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0_READY" in doc
    assert manifest["sentinel"] == ("AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0_READY")

    boundaries = manifest["boundaries"]
    assert boundaries["docs_only"] is True
    assert boundaries["non_executing"] is True
    assert boundaries["non_authorizing"] is True
    assert boundaries["no_contracts_schema_change"] is True
    assert boundaries["no_scanner_implementation"] is True
    assert boundaries["no_formal_registry_activation"] is True
    assert boundaries["no_runtime_behavior_change"] is True


def test_repo_adoption_targets_cover_required_repositories() -> None:
    manifest = _read_manifest()
    targets = manifest["repo_adoption_targets"]

    required_repositories = {
        "aiant-governance",
        "aiant-contracts",
        "aiant-pant",
        "aiant-core",
        "aiant-mmn",
        "aiant-zant",
        "aiant-vant",
        "aiant-drl",
        "aiant-tft",
        "aiant-gant",
        "aiant-marl",
    }
    assert required_repositories.issubset(set(targets))

    assert "lane" in targets["aiant-governance"]
    assert "surface" in targets["aiant-contracts"]
    assert "route" in targets["aiant-pant"]
    assert "path" in targets["aiant-core"]


def test_mmn_zant_vant_adoption_targets_preserve_boundaries() -> None:
    manifest = _read_manifest()
    targets = manifest["repo_adoption_targets"]

    assert "chain" in targets["aiant-mmn"]
    assert "link" in targets["aiant-mmn"]
    assert "seam" in targets["aiant-zant"]
    assert "hint" in targets["aiant-vant"]
    assert "boundary" in targets["aiant-vant"]


def test_future_downstream_preview_repositories_are_mapped() -> None:
    doc = _read_doc()
    manifest = _read_manifest()
    targets = manifest["repo_adoption_targets"]
    preview = manifest["future_downstream_preview_repositories"]

    assert "surface" in targets["aiant-drl"]
    assert "chain" in targets["aiant-drl"]
    assert "no-action-execution boundary" == preview["aiant-drl"]["boundary"]

    assert "sequence" in targets["aiant-tft"]
    assert "window" in targets["aiant-tft"]
    assert "no-live-forecast-consumption boundary" == preview["aiant-tft"]["boundary"]

    assert "graph" in targets["aiant-gant"]
    assert "edge" in targets["aiant-gant"]
    assert "link" in targets["aiant-gant"]
    assert "no-graph-action boundary" == preview["aiant-gant"]["boundary"]

    assert "topology" in targets["aiant-marl"]
    assert "path" in targets["aiant-marl"]
    assert "route" in targets["aiant-marl"]
    assert "no-live-action boundary" == preview["aiant-marl"]["boundary"]

    for repo_name in ["aiant-drl", "aiant-tft", "aiant-gant", "aiant-marl"]:
        assert repo_name in doc


def test_future_downstream_preview_boundary_blocks_runtime_authority() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    required_boundary = {
        "not_connected",
        "not_consuming",
        "not_deciding",
        "not_executing",
        "no_runtime_authority",
        "candidate_preview_surface_only",
    }
    assert required_boundary.issubset(set(manifest["future_downstream_preview_boundary"]))

    for forbidden_phrase in [
        "policy execution chain",
        "live forecast route",
        "graph action route",
        "agent action execution route",
        "runtime policy loop",
        "runtime forecasting pipeline",
        "live graph propagation loop",
        "runtime agent loop",
    ]:
        assert forbidden_phrase in doc


def test_high_risk_confusions_are_explicitly_documented() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    required_confusions = {
        "link_vs_chain",
        "route_vs_path",
        "lineage_vs_trace",
        "bridge_vs_seam",
        "handoff_vs_flow",
        "loop_vs_chain",
        "surface_vs_boundary",
    }
    assert required_confusions.issubset(set(manifest["high_risk_confusions"]))

    for phrase in [
        "link vs chain",
        "route vs path",
        "lineage vs trace",
        "bridge vs seam",
        "handoff vs flow",
        "loop vs chain",
        "surface vs boundary",
    ]:
        assert phrase in doc


def test_review_checklist_keeps_generic_linkage_from_becoming_precise_term() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    assert "generic_zh_linkage_has_precise_english_anchor" in manifest["review_checklist"]
    assert "如果使用“链路”作为中文泛称" in doc
    assert "精确英文术语" in doc
