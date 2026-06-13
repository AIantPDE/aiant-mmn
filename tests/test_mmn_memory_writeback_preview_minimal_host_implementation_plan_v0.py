from __future__ import annotations

import json
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
EVIDENCE = (
    ROOT
    / "docs"
    / "verification"
    / "mmn_memory_writeback_preview_minimal_host_implementation_plan_v0.json"
)


def load_plan() -> dict[str, Any]:
    return json.loads(EVIDENCE.read_text(encoding="utf-8"))


def test_mmn_mbi_b2_p1_identity_and_source_receipt_locked() -> None:
    plan = load_plan()
    identity = plan["identity"]
    source = plan["source_receipt"]

    assert identity == {
        "stage_marker": "STAGE-MBI-26",
        "segment_marker": "MMN-MBI-B2-P1",
        "source_segment_marker": "MBI-B2-R3",
        "lane": "MBI-BI-B2",
        "repo": "aiant-mmn",
        "stage": "Mmn-VB-memory-writeback-preview-minimal-host-implementation-plan-next",
        "implementation_status": (
            "MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION_PLAN_READY"
        ),
    }
    assert source["repo"] == "aiant-core"
    assert source["merge_commit"] == "d28dd7f3c7e396e2dabb4394754a30713f7614bf"
    assert source["sha256"] == ("9960a4ee299c12fd5d0f7318ace35e695bcc21ed1234a6f8dd684a0e9731e1d6")
    assert source["qrsc_closeout_ready"] is True


def test_mmn_mbi_b2_p1_accepts_exactly_one_formally_selected_work_item() -> None:
    selected = load_plan()["selected_work_item"]

    assert selected["selection_count"] == 1
    assert selected["exactly_one_following_host_selected"] is True
    assert selected["work_item_id"] == (
        "MBI-BI-B2-WI-003-MMN-MEMORY-WRITEBACK-PREVIEW-MINIMAL-HOST"
    )
    assert selected["host_repo"] == "aiant-mmn"
    assert selected["business_surface"] == "memory_writeback_preview"
    assert selected["implementation_started"] is False
    assert selected["runtime_authority_granted"] is False


def test_mmn_mbi_b2_p1_plan_is_docs_test_only() -> None:
    implementation_plan = load_plan()["implementation_plan"]

    assert implementation_plan["plan_class"] == (
        "MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION_PLAN"
    )
    assert implementation_plan["decision"] == (
        "ENTER_MMN_MEMORY_WRITEBACK_PREVIEW_MINIMAL_HOST_IMPLEMENTATION"
    )
    assert implementation_plan["implementation_plan_started"] is True
    assert implementation_plan["implementation_plan_completed"] is True
    assert implementation_plan["docs_test_only"] is True
    assert implementation_plan["production_code_changed"] is False
    assert implementation_plan["production_implementation_started"] is False
    assert implementation_plan["minimal_host_implementation_started"] is False


def test_mmn_mbi_b2_p1_future_host_shape_remains_reference_only() -> None:
    shape = load_plan()["implementation_plan"]["future_minimal_host_shape"]

    assert shape["host_role"] == ("LOCAL_READ_SIDE_REFERENCE_ONLY_MEMORY_WRITEBACK_PREVIEW_HOST")
    assert shape["input_posture"] == "repo_local_preview_reference_only"
    assert shape["output_posture"] == "memory_writeback_preview_only"
    assert shape["memory_write_authorized"] is False
    assert shape["runtime_authority_granted"] is False
    assert shape["side_effecting_execution_authorized"] is False


def test_mmn_mbi_b2_p1_retains_closed_boundaries() -> None:
    plan = load_plan()

    assert plan["closed_boundaries"]
    assert all(value is False for value in plan["closed_boundaries"].values())
    assert all(value is False for value in plan["guardrails"].values())


def test_mmn_mbi_b2_p1_routes_to_bounded_local_implementation_only() -> None:
    next_stage = load_plan()["next_after_post_merge_readback"]

    assert next_stage["stage"] == (
        "Mmn-VB-memory-writeback-preview-minimal-host-implementation-next"
    )
    assert next_stage["repo"] == "aiant-mmn"
    assert next_stage["authorized_scope"] == (
        "repo-local read-side/reference-only minimal host implementation"
    )
    assert (
        next_stage[
            "minimal_host_implementation_authorized_after_plan_merge_and_post_merge_readback"
        ]
        is True
    )
    assert next_stage["memory_write_authorized"] is False
    assert next_stage["runtime_authority_granted"] is False
