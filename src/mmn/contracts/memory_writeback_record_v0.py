from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

MEMORY_WRITEBACK_RECORD_VERSION_V0 = "memory_writeback_record_v0"
SOURCE_STAGE_V0 = "memory_writeback_record_v0"

ALLOWED_STORED_MEMORY_LAYERS_V0: tuple[str, ...] = (
    "hot",
    "warm",
    "cold",
    "posterior",
)

ALLOWED_WRITEBACK_STATUS_V0: tuple[str, ...] = (
    "stored",
    "skipped",
    "deferred",
)

ALLOWED_RETENTION_HINTS_V0: tuple[str, ...] = (
    "short_term",
    "medium_term",
    "long_term",
)


@dataclass(frozen=True)
class MemoryWriteBackRecordV0:
    write_back_version: str
    write_back_id: str
    stored_memory_ref: str
    stored_memory_layer: str
    stored_memory_kind: str
    write_back_status: str
    retention_hint: str
    write_back_notes: str
    trace: Mapping[str, object]


def build_memory_writeback_record_v0(
    *,
    write_back_seed: str,
    stored_memory_ref: str,
    stored_memory_layer: str,
    stored_memory_kind: str,
    write_back_status: str,
    retention_hint: str,
    write_back_notes: str = "",
) -> MemoryWriteBackRecordV0:
    if not write_back_seed.strip():
        raise ValueError("missing write_back_seed")
    if not stored_memory_ref.strip():
        raise ValueError("missing stored_memory_ref")
    if stored_memory_layer not in ALLOWED_STORED_MEMORY_LAYERS_V0:
        raise ValueError("unsupported stored_memory_layer")
    if not stored_memory_kind.strip():
        raise ValueError("missing stored_memory_kind")
    if write_back_status not in ALLOWED_WRITEBACK_STATUS_V0:
        raise ValueError("unsupported write_back_status")
    if retention_hint not in ALLOWED_RETENTION_HINTS_V0:
        raise ValueError("unsupported retention_hint")

    write_back_id = f"memory-writeback-record::{write_back_seed.strip()}"

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "write_back_id": write_back_id,
        "stored_memory_ref": stored_memory_ref.strip(),
        "stored_memory_layer": stored_memory_layer,
        "write_back_status": write_back_status,
    }

    return MemoryWriteBackRecordV0(
        write_back_version=MEMORY_WRITEBACK_RECORD_VERSION_V0,
        write_back_id=write_back_id,
        stored_memory_ref=stored_memory_ref.strip(),
        stored_memory_layer=stored_memory_layer,
        stored_memory_kind=stored_memory_kind.strip(),
        write_back_status=write_back_status,
        retention_hint=retention_hint,
        write_back_notes=write_back_notes.strip(),
        trace=trace,
    )


def memory_writeback_record_to_payload_v0(
    write_back_record: MemoryWriteBackRecordV0,
) -> dict[str, object]:
    return {
        "write_back_version": write_back_record.write_back_version,
        "write_back_id": write_back_record.write_back_id,
        "stored_memory_ref": write_back_record.stored_memory_ref,
        "stored_memory_layer": write_back_record.stored_memory_layer,
        "stored_memory_kind": write_back_record.stored_memory_kind,
        "write_back_status": write_back_record.write_back_status,
        "retention_hint": write_back_record.retention_hint,
        "write_back_notes": write_back_record.write_back_notes,
        "trace": dict(write_back_record.trace),
    }


__all__ = [
    "ALLOWED_RETENTION_HINTS_V0",
    "ALLOWED_STORED_MEMORY_LAYERS_V0",
    "ALLOWED_WRITEBACK_STATUS_V0",
    "MEMORY_WRITEBACK_RECORD_VERSION_V0",
    "MemoryWriteBackRecordV0",
    "build_memory_writeback_record_v0",
    "memory_writeback_record_to_payload_v0",
]
