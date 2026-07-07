from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / (
    "docs/terminology/AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0.md"
)
MANIFEST_PATH = ROOT / (
    "docs/terminology/"
    "aiant_linkage_family_terminology_scanner_preparation_"
    "report_only_rules_v0.json"
)


def _read_doc() -> str:
    return DOC_PATH.read_text(encoding="utf-8")


def _read_manifest() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(MANIFEST_PATH.read_text(encoding="utf-8")))


def test_report_only_scanner_preparation_doc_has_sentinel_and_boundaries() -> None:
    doc = _read_doc()

    assert "AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0_READY" in doc
    assert "report-only rules only" in doc
    assert "no scanner implementation" in doc
    assert "no CI gating" in doc
    assert "no automatic replacement" in doc
    assert "non-executing" in doc
    assert "non-authorizing" in doc


def test_manifest_preserves_non_executing_non_authorizing_scope() -> None:
    manifest = _read_manifest()
    scope = cast(dict[str, Any], manifest["scope"])
    scanner_policy = cast(dict[str, Any], manifest["scanner_policy"])

    assert scope["docs_only"] is True
    assert scope["scanner_implementation"] is False
    assert scope["ci_gating"] is False
    assert scope["automatic_replacement"] is False
    assert scope["formal_registry_activation"] is False
    assert scope["contracts_schema_change"] is False
    assert scope["runtime_behavior_change"] is False
    assert scope["cross_repo_file_mutation"] is False
    assert scope["non_executing"] is True
    assert scope["non_authorizing"] is True

    assert scanner_policy["mode"] == "report_only_candidate_rules"
    assert scanner_policy["auto_replace_allowed"] is False
    assert scanner_policy["ci_blocking_allowed"] is False
    assert scanner_policy["deny_runtime_authorization"] is True


def test_rule_candidates_are_report_only_and_non_blocking() -> None:
    manifest = _read_manifest()
    rule_candidates = cast(list[dict[str, Any]], manifest["rule_candidates"])

    assert len(rule_candidates) >= 12
    for rule in rule_candidates:
        assert rule["rule_id"].startswith("RULE-LINKAGE-")
        assert rule["mode"] == "report_only"
        assert rule["severity"] == "review"
        assert rule["auto_replace_allowed"] is False
        assert rule["ci_blocking_allowed"] is False


def test_core_linkage_confusion_rule_families_are_present() -> None:
    manifest = _read_manifest()
    names = {rule["name"] for rule in cast(list[dict[str, Any]], manifest["rule_candidates"])}

    expected = {
        "generic_zh_linkage_without_english_anchor",
        "chain_lane_trace_confusion",
        "path_route_confusion",
        "lineage_trace_provenance_confusion",
        "bridge_seam_handoff_confusion",
        "flow_pipeline_loop_confusion",
        "link_chain_confusion",
        "surface_boundary_confusion",
    }

    assert expected <= names


def test_extended_downstream_report_only_rules_are_present() -> None:
    manifest = _read_manifest()
    rules = cast(list[dict[str, Any]], manifest["rule_candidates"])
    by_name = {rule["name"]: rule for rule in rules}

    assert "graph_edge_link_chain_confusion" in by_name
    assert "tft_sequence_window_chain_confusion" in by_name
    assert "drl_execution_semantics_boundary" in by_name
    assert "marl_live_action_semantics_boundary" in by_name

    gant_rule = by_name["graph_edge_link_chain_confusion"]
    tft_rule = by_name["tft_sequence_window_chain_confusion"]
    drl_rule = by_name["drl_execution_semantics_boundary"]
    marl_rule = by_name["marl_live_action_semantics_boundary"]

    assert "aiant-gant" in cast(list[str], gant_rule["target_repositories"])
    assert "aiant-tft" in cast(list[str], tft_rule["target_repositories"])
    assert "aiant-drl" in cast(list[str], drl_rule["target_repositories"])
    assert "aiant-marl" in cast(list[str], marl_rule["target_repositories"])

    assert "graph execution path" in cast(list[str], gant_rule["forbidden_runtime_semantics"])
    assert "live forecast route" in cast(list[str], tft_rule["forbidden_runtime_semantics"])
    assert "action execution path" in cast(list[str], drl_rule["forbidden_runtime_semantics"])
    assert "runtime agent loop" in cast(list[str], marl_rule["forbidden_runtime_semantics"])


def test_minimum_report_item_schema_is_context_preserving() -> None:
    manifest = _read_manifest()
    fields = set(cast(list[str], manifest["minimum_report_item_fields"]))

    expected = {
        "rule_id",
        "mode",
        "severity",
        "file_path",
        "line_number",
        "matched_text",
        "nearby_context",
        "recommended_review_question",
        "suggested_precise_terms",
        "auto_replace_allowed",
        "ci_blocking_allowed",
        "non_authorizing_note",
    }

    assert expected <= fields


def test_doc_explicitly_says_not_ready_for_activation() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    assert "Not ready for scanner activation" in doc
    not_ready = set(cast(list[str], manifest["not_ready_for_activation"]))

    assert "no scanner CLI" in not_ready
    assert "no scanner engine" in not_ready
    assert "no CI policy" in not_ready
    assert "no governance approval for blocking mode" in not_ready
