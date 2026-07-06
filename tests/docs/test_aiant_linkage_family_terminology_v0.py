from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / "docs" / "terminology" / "AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0.md"
MANIFEST_PATH = ROOT / "docs" / "terminology" / "aiant_linkage_family_terminology_v0.json"


def test_linkage_family_terminology_doc_exists_and_declares_boundary() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    assert "AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0_READY" in text
    assert "terminology-only" in text
    assert "non-executing" in text
    assert "non-authorizing" in text
    assert "no formal field registry" in text or "create formal field registry entries" in text
    assert "change contracts schema" in text
    assert "runtime activation" in text


def test_linkage_family_terms_are_distinguished() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_pairs = {
        "chain": "有序链",
        "lane": "治理路线",
        "trace": "可追溯轨迹",
        "path": "路径",
        "route": "路由",
        "flow": "信息流",
        "pipeline": "管线",
        "lineage": "血缘",
        "provenance": "来源证明",
        "bridge": "桥接",
        "seam": "接缝",
        "handoff": "移交",
        "loop": "闭环",
        "link": "关联",
        "surface": "暴露面",
        "boundary": "边界",
    }

    for english, chinese in expected_pairs.items():
        assert english in text
        assert chinese in text


def test_linkage_family_normative_rules_are_present() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    assert "chain = method/order" in text
    assert "lane  = work-family classification" in text
    assert "trace = replayable history" in text
    assert "path 关注可达性" in text
    assert "route 关注选择、准入和拒绝" in text
    assert "lineage answers: derived from what?" in text
    assert "provenance answers: origin proven by what?" in text
    assert "bridge = cross-layer connection" in text
    assert "seam = thin interface" in text
    assert "handoff = upstream-to-downstream transfer" in text
    assert "flow moves" in text
    assert "pipeline processes in stages" in text
    assert "loop returns feedback" in text
    assert "link = one relation" in text
    assert "chain = ordered relation sequence" in text
    assert "surface says what is consumable" in text
    assert "boundary says what must not be crossed" in text


def test_linkage_family_manifest_matches_doc_boundary_and_terms() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    text = DOC_PATH.read_text(encoding="utf-8")

    assert manifest["terminology_record_id"] == "AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0"
    assert manifest["sentinel"] == "AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0_READY"
    assert manifest["sentinel"] in text

    boundary = set(manifest["boundary"])
    assert "docs_only" in boundary
    assert "terminology_only" in boundary
    assert "non_executing" in boundary
    assert "non_authorizing" in boundary
    assert "no_contract_schema_change" in boundary
    assert "no_field_registry_update" in boundary
    assert "no_runtime_activation" in boundary

    required_terms = {
        "chain",
        "lane",
        "trace",
        "path",
        "route",
        "flow",
        "pipeline",
        "lineage",
        "provenance",
        "audit_trail",
        "bridge",
        "seam",
        "handoff",
        "loop",
        "link",
        "surface",
        "boundary",
    }
    assert required_terms <= set(manifest["canonical_terms"])

    assert manifest["canonical_terms"]["chain"]["preferred_cn"][0] == "有序链"
    assert manifest["canonical_terms"]["lane"]["preferred_cn"][0] == "治理路线"
    assert manifest["canonical_terms"]["trace"]["preferred_cn"][0] == "可追溯轨迹"
    assert manifest["canonical_terms"]["route"]["preferred_cn"][0] == "路由"
    assert manifest["canonical_terms"]["lineage"]["preferred_cn"][0] == "血缘"


def test_forbidden_over_translation_examples_are_explicit() -> None:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
    text = DOC_PATH.read_text(encoding="utf-8")

    examples = manifest["forbidden_over_translation_examples"]
    assert any("route_preview" in example for example in examples)
    assert any("execution_handoff_envelope" in example for example in examples)
    assert any("attribution_link_ref" in example for example in examples)
    assert any("feedback validation loop" in example for example in examples)
    assert any("non-authorizing boundary" in example for example in examples)

    for phrase in [
        "route_preview",
        "execution_handoff_envelope",
        "attribution_link_ref",
        "feedback validation loop",
        "non-authorizing boundary",
    ]:
        assert phrase in text
