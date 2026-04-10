from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

MEMORY_RECORD_VERSION_V0 = "memory_record_v0"
SOURCE_STAGE_V0 = "memory_record_v0"

ALLOWED_RECORD_KINDS_V0: tuple[str, ...] = (
    "evidence_note",
    "summary_note",
    "trace_note",
    "citation_note",
)


@dataclass(frozen=True)
class MemoryRecordV0:
    record_version: str
    record_id: str
    record_kind: str
    record_text: str
    reason_codes: tuple[str, ...]
    trace: Mapping[str, object]


def normalize_str_tuple_v0(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        item = value.strip()
        return (item,) if item else ()

    normalized: list[str] = []
    try:
        for item in value:  # type: ignore[assignment]
            if isinstance(item, str):
                stripped = item.strip()
                if stripped:
                    normalized.append(stripped)
    except TypeError:
        return ()
    return tuple(normalized)


def build_memory_record_v0(
    *,
    record_seed: str,
    record_kind: str,
    record_text: str,
    reason_codes: tuple[str, ...] | list[str] = (),
) -> MemoryRecordV0:
    if not record_seed.strip():
        raise ValueError("missing record_seed")
    if record_kind not in ALLOWED_RECORD_KINDS_V0:
        raise ValueError("unsupported record_kind")
    if not record_text.strip():
        raise ValueError("missing record_text")

    normalized_reason_codes = normalize_str_tuple_v0(reason_codes)
    record_id = f"memory-record::{record_seed.strip()}"

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "record_id": record_id,
        "record_kind": record_kind,
        "record_text": record_text.strip(),
        "reason_codes": normalized_reason_codes,
    }

    return MemoryRecordV0(
        record_version=MEMORY_RECORD_VERSION_V0,
        record_id=record_id,
        record_kind=record_kind,
        record_text=record_text.strip(),
        reason_codes=normalized_reason_codes,
        trace=trace,
    )


def memory_record_to_payload_v0(record: MemoryRecordV0) -> dict[str, object]:
    return {
        "record_version": record.record_version,
        "record_id": record.record_id,
        "record_kind": record.record_kind,
        "record_text": record.record_text,
        "reason_codes": tuple(record.reason_codes),
        "trace": dict(record.trace),
    }


__all__ = [
    "ALLOWED_RECORD_KINDS_V0",
    "MEMORY_RECORD_VERSION_V0",
    "MemoryRecordV0",
    "build_memory_record_v0",
    "memory_record_to_payload_v0",
    "normalize_str_tuple_v0",
]
