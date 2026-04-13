from __future__ import annotations

import pytest

from mmn.contracts.memory_writeback_record_v0 import (
    build_memory_writeback_record_v0,
)


def test_memory_writeback_record_rejects_empty_seed() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_record_v0(
            write_back_seed="",
            stored_memory_ref="mem_alpha",
            stored_memory_layer="posterior",
            stored_memory_kind="posterior_memory_note",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_memory_writeback_record_rejects_empty_stored_memory_ref() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="",
            stored_memory_layer="posterior",
            stored_memory_kind="posterior_memory_note",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_memory_writeback_record_rejects_invalid_layer() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_alpha",
            stored_memory_layer="invalid_layer",
            stored_memory_kind="posterior_memory_note",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_memory_writeback_record_rejects_invalid_status() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_alpha",
            stored_memory_layer="posterior",
            stored_memory_kind="posterior_memory_note",
            write_back_status="invalid_status",
            retention_hint="long_term",
        )


def test_memory_writeback_record_rejects_invalid_retention_hint() -> None:
    with pytest.raises(ValueError):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_alpha",
            stored_memory_layer="posterior",
            stored_memory_kind="posterior_memory_note",
            write_back_status="stored",
            retention_hint="forever",
        )


def test_memory_writeback_record_builds_minimal_valid_object() -> None:
    obj = build_memory_writeback_record_v0(
        write_back_seed="alpha",
        stored_memory_ref="mem_alpha",
        stored_memory_layer="posterior",
        stored_memory_kind="posterior_memory_note",
        write_back_status="stored",
        retention_hint="long_term",
        write_back_notes="alpha note",
    )

    assert obj.write_back_id == "memory-writeback-record::alpha"
    assert obj.stored_memory_ref == "mem_alpha"
    assert obj.stored_memory_layer == "posterior"
    assert obj.write_back_status == "stored"
    assert obj.retention_hint == "long_term"
    assert obj.trace["source_stage"] == "memory_writeback_record_v0"
