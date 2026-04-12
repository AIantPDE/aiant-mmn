from dataclasses import asdict, fields

import pytest

from mmn.contracts.memory_writeback_request_v0 import (
    build_memory_writeback_request_v0,
    memory_writeback_request_to_payload_v0,
)


def test_memory_writeback_request_shape_is_stable() -> None:
    write_back_request = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id="subject-alpha",
        write_back_reason=("posterior_update_required",),
        target_memory_layer=("posterior", "cold"),
        source_evidence_refs=("outcome_trace_001", "post_action_diagnosis_001"),
        write_back_mode="structured_posterior_update",
    )

    field_names = tuple(field.name for field in fields(write_back_request))
    assert field_names == (
        "write_back_version",
        "write_back_id",
        "subject_id",
        "write_back_reason",
        "target_memory_layer",
        "source_evidence_refs",
        "write_back_mode",
        "trace",
    )

    payload = asdict(write_back_request)
    assert payload["write_back_version"] == "memory_writeback_request_v0"
    assert payload["write_back_id"] == "memory-writeback::alpha"


def test_build_memory_writeback_request_v0_rejects_blank_write_back_seed() -> None:
    with pytest.raises(ValueError, match="missing write_back_seed"):
        build_memory_writeback_request_v0(
            write_back_seed="   ",
            subject_id="subject-alpha",
            write_back_mode="preview_only",
        )


def test_build_memory_writeback_request_v0_rejects_blank_subject_id() -> None:
    with pytest.raises(ValueError, match="missing subject_id"):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="   ",
            write_back_mode="preview_only",
        )


def test_build_memory_writeback_request_v0_rejects_unsupported_write_back_mode() -> None:
    with pytest.raises(ValueError, match="unsupported write_back_mode"):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="subject-alpha",
            write_back_mode="store_now",
        )


def test_build_memory_writeback_request_v0_rejects_unsupported_target_memory_layer() -> None:
    with pytest.raises(ValueError, match="unsupported target_memory_layer"):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="subject-alpha",
            target_memory_layer=("archive",),
            write_back_mode="preview_only",
        )


def test_build_memory_writeback_request_v0_normalizes_tuple_fields() -> None:
    write_back_request = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id=" subject-alpha ",
        write_back_reason=[" posterior_update_required ", "", "failed_chain_sync_exemplar"],
        target_memory_layer=[" posterior ", "", "cold"],
        source_evidence_refs=[" outcome_trace_001 ", "", "post_action_diagnosis_001"],
        write_back_mode="structured_posterior_update",
    )

    assert write_back_request.subject_id == "subject-alpha"
    assert write_back_request.write_back_reason == (
        "posterior_update_required",
        "failed_chain_sync_exemplar",
    )
    assert write_back_request.target_memory_layer == ("posterior", "cold")
    assert write_back_request.source_evidence_refs == (
        "outcome_trace_001",
        "post_action_diagnosis_001",
    )


def test_memory_writeback_request_payload_projection_is_stable() -> None:
    write_back_request = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id="subject-alpha",
        write_back_reason=("posterior_update_required", "failed_chain_sync_exemplar"),
        target_memory_layer=("posterior", "cold"),
        source_evidence_refs=("outcome_trace_001", "post_action_diagnosis_001"),
        write_back_mode="structured_posterior_update",
    )

    payload = memory_writeback_request_to_payload_v0(write_back_request)

    assert payload == {
        "write_back_version": "memory_writeback_request_v0",
        "write_back_id": "memory-writeback::alpha",
        "subject_id": "subject-alpha",
        "write_back_reason": (
            "posterior_update_required",
            "failed_chain_sync_exemplar",
        ),
        "target_memory_layer": ("posterior", "cold"),
        "source_evidence_refs": (
            "outcome_trace_001",
            "post_action_diagnosis_001",
        ),
        "write_back_mode": "structured_posterior_update",
        "trace": {
            "source_stage": "memory_writeback_request_v0",
            "write_back_id": "memory-writeback::alpha",
            "subject_id": "subject-alpha",
            "write_back_mode": "structured_posterior_update",
            "target_memory_layer_count": 2,
            "source_evidence_ref_count": 2,
        },
    }
