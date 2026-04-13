from __future__ import annotations

import pytest

from mmn.contracts.memory_writeback_request_v0 import (
    build_memory_writeback_request_v0,
)


def test_memory_writeback_request_rejects_empty_seed() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_request_v0(
            write_back_seed="",
            subject_id="subject-alpha",
            write_back_mode="preview_only",
        )


def test_memory_writeback_request_rejects_empty_subject_id() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="",
            write_back_mode="preview_only",
        )


def test_memory_writeback_request_rejects_invalid_mode() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="subject-alpha",
            write_back_mode="invalid_mode",
        )


def test_memory_writeback_request_rejects_invalid_target_memory_layer() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_request_v0(
            write_back_seed="alpha",
            subject_id="subject-alpha",
            target_memory_layer=("posterior", "invalid_layer"),
            write_back_mode="preview_only",
        )


def test_memory_writeback_request_normalizes_minimal_sequences() -> None:
    obj = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id="subject-alpha",
        write_back_reason=("posterior_update_required", "posterior_update_required"),
        target_memory_layer=("posterior", "cold", "posterior"),
        source_evidence_refs=("ref-1", "ref-1", "ref-2"),
        write_back_mode="structured_posterior_update",
    )

    assert obj.write_back_id == "memory-writeback::alpha"
    assert obj.subject_id == "subject-alpha"
    assert obj.write_back_mode == "structured_posterior_update"
    assert all(layer in {"hot", "warm", "cold", "posterior"} for layer in obj.target_memory_layer)
    assert len(obj.target_memory_layer) >= 1
    assert obj.trace["source_stage"] == "memory_writeback_request_v0"
