from dataclasses import asdict, fields

import pytest

from mmn.contracts.memory_writeback_record_v0 import (
    build_memory_writeback_record_v0,
    memory_writeback_record_to_payload_v0,
)


def test_memory_writeback_record_shape_is_stable() -> None:
    write_back_record = build_memory_writeback_record_v0(
        write_back_seed="alpha",
        stored_memory_ref="mem_posterior_core_vs_chain_lag_003",
        stored_memory_layer="posterior",
        stored_memory_kind="propagation_realization_correction",
        write_back_status="stored",
        retention_hint="long_term",
        write_back_notes="core asset tends to realize earlier than chain spread",
    )

    field_names = tuple(field.name for field in fields(write_back_record))
    assert field_names == (
        "write_back_version",
        "write_back_id",
        "stored_memory_ref",
        "stored_memory_layer",
        "stored_memory_kind",
        "write_back_status",
        "retention_hint",
        "write_back_notes",
        "trace",
    )

    payload = asdict(write_back_record)
    assert payload["write_back_version"] == "memory_writeback_record_v0"
    assert payload["write_back_id"] == "memory-writeback-record::alpha"


def test_build_memory_writeback_record_v0_rejects_blank_write_back_seed() -> None:
    with pytest.raises(ValueError, match="missing write_back_seed"):
        build_memory_writeback_record_v0(
            write_back_seed="   ",
            stored_memory_ref="mem_ref",
            stored_memory_layer="posterior",
            stored_memory_kind="kind",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_build_memory_writeback_record_v0_rejects_blank_stored_memory_ref() -> None:
    with pytest.raises(ValueError, match="missing stored_memory_ref"):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="   ",
            stored_memory_layer="posterior",
            stored_memory_kind="kind",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_build_memory_writeback_record_v0_rejects_unsupported_stored_memory_layer() -> None:
    with pytest.raises(ValueError, match="unsupported stored_memory_layer"):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_ref",
            stored_memory_layer="archive",
            stored_memory_kind="kind",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_build_memory_writeback_record_v0_rejects_blank_stored_memory_kind() -> None:
    with pytest.raises(ValueError, match="missing stored_memory_kind"):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_ref",
            stored_memory_layer="posterior",
            stored_memory_kind="   ",
            write_back_status="stored",
            retention_hint="long_term",
        )


def test_build_memory_writeback_record_v0_rejects_unsupported_write_back_status() -> None:
    with pytest.raises(ValueError, match="unsupported write_back_status"):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_ref",
            stored_memory_layer="posterior",
            stored_memory_kind="kind",
            write_back_status="written",
            retention_hint="long_term",
        )


def test_build_memory_writeback_record_v0_rejects_unsupported_retention_hint() -> None:
    with pytest.raises(ValueError, match="unsupported retention_hint"):
        build_memory_writeback_record_v0(
            write_back_seed="alpha",
            stored_memory_ref="mem_ref",
            stored_memory_layer="posterior",
            stored_memory_kind="kind",
            write_back_status="stored",
            retention_hint="forever",
        )


def test_build_memory_writeback_record_v0_normalizes_string_fields() -> None:
    write_back_record = build_memory_writeback_record_v0(
        write_back_seed=" alpha ",
        stored_memory_ref=" mem_ref ",
        stored_memory_layer="posterior",
        stored_memory_kind=" propagation_realization_correction ",
        write_back_status="stored",
        retention_hint="medium_term",
        write_back_notes=" stored note ",
    )

    assert write_back_record.write_back_id == "memory-writeback-record::alpha"
    assert write_back_record.stored_memory_ref == "mem_ref"
    assert write_back_record.stored_memory_kind == "propagation_realization_correction"
    assert write_back_record.write_back_notes == "stored note"


def test_memory_writeback_record_payload_projection_is_stable() -> None:
    write_back_record = build_memory_writeback_record_v0(
        write_back_seed="alpha",
        stored_memory_ref="mem_posterior_core_vs_chain_lag_003",
        stored_memory_layer="posterior",
        stored_memory_kind="propagation_realization_correction",
        write_back_status="stored",
        retention_hint="long_term",
        write_back_notes="core asset tends to realize earlier than chain spread",
    )

    payload = memory_writeback_record_to_payload_v0(write_back_record)

    assert payload == {
        "write_back_version": "memory_writeback_record_v0",
        "write_back_id": "memory-writeback-record::alpha",
        "stored_memory_ref": "mem_posterior_core_vs_chain_lag_003",
        "stored_memory_layer": "posterior",
        "stored_memory_kind": "propagation_realization_correction",
        "write_back_status": "stored",
        "retention_hint": "long_term",
        "write_back_notes": "core asset tends to realize earlier than chain spread",
        "trace": {
            "source_stage": "memory_writeback_record_v0",
            "write_back_id": "memory-writeback-record::alpha",
            "stored_memory_ref": "mem_posterior_core_vs_chain_lag_003",
            "stored_memory_layer": "posterior",
            "write_back_status": "stored",
        },
    }
