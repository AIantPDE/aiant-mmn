from __future__ import annotations

from typing import cast

from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.memory_writeback_record_v0 import (
    build_memory_writeback_record_v0,
    memory_writeback_record_to_payload_v0,
)


def test_memory_writeback_record_payload_v0_minimal_projection() -> None:
    obj = build_memory_writeback_record_v0(
        write_back_seed="alpha",
        stored_memory_ref="mem_alpha",
        stored_memory_layer="warm",
        stored_memory_kind="preview_memory_note",
        write_back_status="deferred",
        retention_hint="short_term",
    )

    payload = cast(dict[str, object], memory_writeback_record_to_payload_v0(obj))

    assert payload["write_back_version"] == "memory_writeback_record_v0"
    assert payload["write_back_id"] == "memory-writeback-record::alpha"
    assert payload["stored_memory_ref"] == "mem_alpha"
    assert payload["stored_memory_layer"] == "warm"
    assert payload["stored_memory_kind"] == "preview_memory_note"
    assert payload["write_back_status"] == "deferred"
    assert payload["retention_hint"] == "short_term"
    assert payload["write_back_notes"] == ""

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "memory_writeback_record_v0"
    assert trace["write_back_id"] == "memory-writeback-record::alpha"
    assert trace["stored_memory_ref"] == "mem_alpha"
    assert trace["stored_memory_layer"] == "warm"
    assert trace["write_back_status"] == "deferred"

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_memory_writeback_record_payload_v0_stored_projection() -> None:
    obj = build_memory_writeback_record_v0(
        write_back_seed="beta",
        stored_memory_ref="mem_posterior_beta",
        stored_memory_layer="posterior",
        stored_memory_kind="propagation_realization_correction",
        write_back_status="stored",
        retention_hint="long_term",
        write_back_notes="core asset tends to realize earlier than chain spread",
    )

    payload = cast(dict[str, object], memory_writeback_record_to_payload_v0(obj))

    assert payload["write_back_version"] == "memory_writeback_record_v0"
    assert payload["write_back_id"] == "memory-writeback-record::beta"
    assert payload["stored_memory_ref"] == "mem_posterior_beta"
    assert payload["stored_memory_layer"] == "posterior"
    assert payload["stored_memory_kind"] == "propagation_realization_correction"
    assert payload["write_back_status"] == "stored"
    assert payload["retention_hint"] == "long_term"
    assert payload["write_back_notes"] == ("core asset tends to realize earlier than chain spread")

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "memory_writeback_record_v0"
    assert trace["write_back_id"] == "memory-writeback-record::beta"
    assert trace["stored_memory_ref"] == "mem_posterior_beta"
    assert trace["stored_memory_layer"] == "posterior"
    assert trace["write_back_status"] == "stored"

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_memory_writeback_record_payload_v0_trace_matches_payload_core_fields() -> None:
    obj = build_memory_writeback_record_v0(
        write_back_seed="gamma",
        stored_memory_ref="mem_gamma",
        stored_memory_layer="cold",
        stored_memory_kind="historical_failure_note",
        write_back_status="deferred",
        retention_hint="short_term",
        write_back_notes="gamma note",
    )

    payload = cast(dict[str, object], memory_writeback_record_to_payload_v0(obj))
    trace = cast(dict[str, object], payload["trace"])

    assert trace["source_stage"] == "memory_writeback_record_v0"
    assert trace["write_back_id"] == payload["write_back_id"]
    assert trace["stored_memory_ref"] == payload["stored_memory_ref"]
    assert trace["stored_memory_layer"] == payload["stored_memory_layer"]
    assert trace["write_back_status"] == payload["write_back_status"]

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload
