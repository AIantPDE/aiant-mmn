from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

from mmn.contracts.memory_record_v0 import MemoryRecordV0

MEMORY_OUTPUT_VERSION_V0 = "memory_preview_output_v0"
MEMORY_OUTPUT_MODEL_VERSION_V0 = "memory_preview_output_model_v0"
SOURCE_STAGE_V0 = "memory_preview_output_v0"

ALLOWED_MEMORY_STRENGTH_HINTS_V0: tuple[str, ...] = (
    "weak",
    "medium",
    "strong",
)

ALLOWED_CITATION_HINTS_V0: tuple[str, ...] = (
    "none",
    "limited",
    "available",
)


@dataclass(frozen=True)
class MemoryPreviewOutputV0:
    memory_output_version: str
    memory_output_model_version: str
    memory_output_id: str
    records: tuple[MemoryRecordV0, ...]
    memory_strength_hint: str
    citation_hint: str
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


def build_memory_preview_output_v0(
    *,
    output_seed: str,
    records: tuple[MemoryRecordV0, ...] | list[MemoryRecordV0],
    memory_strength_hint: str,
    citation_hint: str,
    reason_codes: tuple[str, ...] | list[str] = (),
) -> MemoryPreviewOutputV0:
    if not output_seed.strip():
        raise ValueError("missing output_seed")
    if memory_strength_hint not in ALLOWED_MEMORY_STRENGTH_HINTS_V0:
        raise ValueError("unsupported memory_strength_hint")
    if citation_hint not in ALLOWED_CITATION_HINTS_V0:
        raise ValueError("unsupported citation_hint")

    records_t = tuple(records)
    normalized_reason_codes = normalize_str_tuple_v0(reason_codes)
    memory_output_id = f"memory-preview::{output_seed.strip()}"

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "memory_output_id": memory_output_id,
        "record_count": len(records_t),
        "memory_strength_hint": memory_strength_hint,
        "citation_hint": citation_hint,
        "reason_codes": normalized_reason_codes,
    }

    return MemoryPreviewOutputV0(
        memory_output_version=MEMORY_OUTPUT_VERSION_V0,
        memory_output_model_version=MEMORY_OUTPUT_MODEL_VERSION_V0,
        memory_output_id=memory_output_id,
        records=records_t,
        memory_strength_hint=memory_strength_hint,
        citation_hint=citation_hint,
        reason_codes=normalized_reason_codes,
        trace=trace,
    )


__all__ = [
    "ALLOWED_CITATION_HINTS_V0",
    "ALLOWED_MEMORY_STRENGTH_HINTS_V0",
    "MEMORY_OUTPUT_MODEL_VERSION_V0",
    "MEMORY_OUTPUT_VERSION_V0",
    "MemoryPreviewOutputV0",
    "build_memory_preview_output_v0",
    "normalize_str_tuple_v0",
]
