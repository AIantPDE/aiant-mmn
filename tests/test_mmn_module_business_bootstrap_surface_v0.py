from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[1]
JSON_PATH = ROOT / "docs" / "verification" / "mmn_module_business_bootstrap_surface_v0.json"
DOC_PATH = ROOT / "docs" / "verification" / "MMN_MODULE_BUSINESS_BOOTSTRAP_SURFACE_V0.md"


def load() -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(JSON_PATH.read_text(encoding="utf-8")))


def test_files_exist() -> None:
    assert JSON_PATH.exists()
    assert DOC_PATH.exists()


def test_identity_locked() -> None:
    bundle = load()
    assert bundle["stage_marker"] == "STAGE-MBI-09"
    assert bundle["segment_marker"] == "MBI-08"
    assert bundle["source_segment_marker"] == "MBI-07"
    assert bundle["repo"] == "aiant-mmn"
    assert bundle["stage"] == "MMN-VB-mmn-module-business-bootstrap-surface-next"


def test_predecessors_locked() -> None:
    bundle = load()
    assert bundle["source_pant_mbi05_validated"] is True
    assert bundle["source_vant_mbi06_validated"] is True
    assert bundle["source_zant_mbi07_validated"] is True


def test_surface_status_locked() -> None:
    bundle = load()
    assert bundle["surface_status"] == "MMN_MODULE_BUSINESS_BOOTSTRAP_SURFACE_READY"
    assert bundle["surface_type"] == "DOCS_TEST_MODULE_BUSINESS_BOOTSTRAP_SURFACE"
    assert bundle["surface_scope"] == "MMN_MEMORY_PREVIEW_AND_WRITEBACK_HOST"
    assert len(bundle["surface_capabilities"]) == 4


def test_authority_closed() -> None:
    bundle = load()
    assert bundle["non_executing"] is True
    assert bundle["non_side_effect"] is True
    assert bundle["docs_test_only"] is True
    assert bundle["production_code_changed"] is False
    assert bundle["contract_schema_changed"] is False
    assert bundle["runtime_loader_changed"] is False
    assert bundle["memory_writeback_execution_started"] is False
    assert bundle["worker_activation_started"] is False
    assert bundle["github_write_api_called_by_mbi08"] is False
    assert bundle["branch_protection_mutation_started_by_mbi08"] is False
    assert bundle["ruleset_mutation_started"] is False
    assert bundle["runtime_authority_granted"] is False


def test_next_stage_locked() -> None:
    bundle = load()
    assert bundle["recommended_next_stage"] == (
        "Gant-VB-gant-module-business-bootstrap-surface-next"
    )
    assert bundle["recommended_next_stage_repo"] == "aiant-gant"
