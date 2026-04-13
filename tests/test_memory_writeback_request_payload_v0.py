from __future__ import annotations

from typing import cast

from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.memory_writeback_request_v0 import (
    build_memory_writeback_request_v0,
    memory_writeback_request_to_payload_v0,
)


def test_memory_writeback_request_payload_v0_minimal_projection() -> None:
    obj = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id="subject-alpha",
        write_back_mode="preview_only",
    )

    payload = cast(dict[str, object], memory_writeback_request_to_payload_v0(obj))

    assert payload["write_back_version"] == "memory_writeback_request_v0"
    assert payload["write_back_id"] == "memory-writeback::alpha"
    assert payload["subject_id"] == "subject-alpha"
    assert payload["write_back_reason"] == ()
    assert payload["target_memory_layer"] == ()
    assert payload["source_evidence_refs"] == ()
    assert payload["write_back_mode"] == "preview_only"

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "memory_writeback_request_v0"
    assert trace["write_back_id"] == "memory-writeback::alpha"
    assert trace["subject_id"] == "subject-alpha"
    assert trace["write_back_mode"] == "preview_only"
    assert trace["target_memory_layer_count"] == 0
    assert trace["source_evidence_ref_count"] == 0

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_memory_writeback_request_payload_v0_richer_projection() -> None:
    obj = build_memory_writeback_request_v0(
        write_back_seed="beta",
        subject_id="subject-beta",
        write_back_reason=(
            "posterior_update_required",
            "failed_chain_sync_exemplar",
        ),
        target_memory_layer=("posterior", "cold"),
        source_evidence_refs=(
            "posterior-correction::beta",
            "historical-comparison::beta",
            "outcome-trace::beta",
        ),
        write_back_mode="structured_posterior_update",
    )

    payload = cast(dict[str, object], memory_writeback_request_to_payload_v0(obj))

    assert payload["write_back_version"] == "memory_writeback_request_v0"
    assert payload["write_back_id"] == "memory-writeback::beta"
    assert payload["subject_id"] == "subject-beta"
    assert payload["write_back_reason"] == (
        "posterior_update_required",
        "failed_chain_sync_exemplar",
    )
    assert payload["target_memory_layer"] == ("posterior", "cold")
    assert payload["source_evidence_refs"] == (
        "posterior-correction::beta",
        "historical-comparison::beta",
        "outcome-trace::beta",
    )
    assert payload["write_back_mode"] == "structured_posterior_update"

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "memory_writeback_request_v0"
    assert trace["write_back_id"] == "memory-writeback::beta"
    assert trace["subject_id"] == "subject-beta"
    assert trace["write_back_mode"] == "structured_posterior_update"
    assert trace["target_memory_layer_count"] == 2
    assert trace["source_evidence_ref_count"] == 3

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_memory_writeback_request_payload_v0_reflects_normalized_counts() -> None:
    obj = build_memory_writeback_request_v0(
        write_back_seed="gamma",
        subject_id="subject-gamma",
        write_back_reason=(
            "posterior_update_required",
            "posterior_update_required",
        ),
        target_memory_layer=("posterior", "cold", "posterior"),
        source_evidence_refs=("ref-1", "ref-1", "ref-2"),
        write_back_mode="structured_posterior_update",
    )

    payload = cast(dict[str, object], memory_writeback_request_to_payload_v0(obj))
    trace = cast(dict[str, object], payload["trace"])
    target_memory_layer = cast(tuple[str, ...], payload["target_memory_layer"])
    source_evidence_refs = cast(tuple[str, ...], payload["source_evidence_refs"])

    assert trace["source_stage"] == "memory_writeback_request_v0"
    assert trace["target_memory_layer_count"] == len(target_memory_layer)
    assert trace["source_evidence_ref_count"] == len(source_evidence_refs)

    for layer in target_memory_layer:
        assert layer in {"hot", "warm", "cold", "posterior"}

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload
