import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]
DOC_PATH = ROOT / (
    "docs/terminology/AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_REPORT_BASELINE_SAMPLE_V0.md"
)
MANIFEST_PATH = ROOT / (
    "docs/terminology/aiant_linkage_family_terminology_scanner_report_baseline_sample_v0.json"
)


def _read_doc() -> str:
    return DOC_PATH.read_text(encoding="utf-8")


def _read_manifest() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(MANIFEST_PATH.read_text(encoding="utf-8")))


def test_scanner_report_baseline_sample_docs_exist() -> None:
    assert DOC_PATH.exists()
    assert MANIFEST_PATH.exists()


def test_scanner_report_baseline_sample_boundary_is_non_executing() -> None:
    doc = _read_doc()
    manifest = _read_manifest()
    boundary = cast(dict[str, bool], manifest["boundary"])

    assert "static sample only" in doc
    assert "no scanner runtime" in doc
    assert boundary["static_sample_only"] is True
    assert boundary["non_executing"] is True
    assert boundary["non_authorizing"] is True
    assert boundary["no_scanner_cli"] is True
    assert boundary["no_scanner_engine"] is True
    assert boundary["no_file_traversal"] is True
    assert boundary["no_match_engine"] is True
    assert boundary["no_ci_gating"] is True
    assert boundary["no_blocking_mode"] is True
    assert boundary["no_auto_replacement"] is True
    assert boundary["synthetic_examples_only"] is True


def test_scanner_report_sample_has_required_upstream_assets() -> None:
    manifest = _read_manifest()
    upstream_assets = set(cast(list[str], manifest["upstream_assets"]))

    assert "AIANT_LINKAGE_FAMILY_TERMINOLOGY_V0" in upstream_assets
    assert "AIANT_LINKAGE_FAMILY_CROSS_REPO_ADOPTION_CHECKLIST_V0" in upstream_assets
    assert (
        "AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_PREPARATION_REPORT_ONLY_RULES_V0"
        in upstream_assets
    )


def test_scanner_report_sample_summary_contract() -> None:
    manifest = _read_manifest()
    sample_report = cast(dict[str, Any], manifest["sample_report"])
    summary = cast(dict[str, Any], sample_report["summary"])

    assert sample_report["report_kind"] == "static_sample"
    assert sample_report["scanner_mode"] == "report_only_sample"
    assert sample_report["execution_state"] == "non_executing"
    assert sample_report["blocking_state"] == "non_blocking"
    assert sample_report["source_scope"] == "synthetic_examples_only"
    assert summary["total_findings"] == 5
    assert summary["blocking_findings"] == 0
    assert summary["synthetic_sample"] is True
    assert summary["activation_ready"] is False


def test_scanner_report_item_minimum_fields_are_declared() -> None:
    manifest = _read_manifest()
    sample_report = cast(dict[str, Any], manifest["sample_report"])
    minimum_fields = set(cast(list[str], sample_report["minimum_report_item_fields"]))

    expected_fields = {
        "finding_id",
        "rule_id",
        "rule_name",
        "severity",
        "repo",
        "file_path",
        "line",
        "matched_text",
        "expected_term",
        "recommendation",
        "blocking",
        "sample_only",
    }

    assert expected_fields <= minimum_fields


def test_synthetic_findings_are_report_only_and_non_blocking() -> None:
    manifest = _read_manifest()
    sample_report = cast(dict[str, Any], manifest["sample_report"])
    findings = cast(list[dict[str, Any]], sample_report["sample_findings"])

    assert len(findings) == 5
    assert all(finding["blocking"] is False for finding in findings)
    assert all(finding["sample_only"] is True for finding in findings)
    assert all("SYNTHETIC_ONLY.md" in finding["file_path"] for finding in findings)


def test_synthetic_findings_cover_high_risk_rule_examples() -> None:
    manifest = _read_manifest()
    sample_report = cast(dict[str, Any], manifest["sample_report"])
    findings = cast(list[dict[str, Any]], sample_report["sample_findings"])
    rule_ids = {finding["rule_id"] for finding in findings}
    repos = {finding["repo"] for finding in findings}

    assert "RULE-LINKAGE-001" in rule_ids
    assert "RULE-LINKAGE-002" in rule_ids
    assert "RULE-LINKAGE-003" in rule_ids
    assert "RULE-LINKAGE-009" in rule_ids
    assert "RULE-LINKAGE-011" in rule_ids
    assert {"aiant-mmn", "aiant-pant", "aiant-gant", "aiant-drl"} <= repos


def test_document_declares_not_ready_for_activation() -> None:
    doc = _read_doc()
    manifest = _read_manifest()
    promotion_conditions = cast(list[str], manifest["promotion_conditions"])

    assert "Blocking mode requires a separate governance decision" in doc
    assert "scanner CLI" in doc
    assert "match engine" in doc
    assert "CI policy" in doc
    assert "cross-repo rollout plan" in doc
    assert "governance approval for report-only scanner scope" in promotion_conditions
    assert "cross-repo rollout plan" in promotion_conditions


def test_sentinel_is_present_in_doc_and_manifest() -> None:
    doc = _read_doc()
    manifest = _read_manifest()

    sentinel = "AIANT_LINKAGE_FAMILY_TERMINOLOGY_SCANNER_REPORT_BASELINE_SAMPLE_V0_READY"
    assert sentinel in doc
    assert manifest["sentinel"] == sentinel
