from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

MEMORY_WRITEBACK_REQUEST_VERSION_V0 = "memory_writeback_request_v0"
SOURCE_STAGE_V0 = "memory_writeback_request_v0"

ALLOWED_TARGET_MEMORY_LAYERS_V0: tuple[str, ...] = (
    "hot",
    "warm",
    "cold",
    "posterior",
)

ALLOWED_WRITEBACK_MODES_V0: tuple[str, ...] = (
    "preview_only",
    "structured_posterior_update",
)


@dataclass(frozen=True)
class MemoryWriteBackRequestV0:
    write_back_version: str
    write_back_id: str
    subject_id: str
    write_back_reason: tuple[str, ...]
    target_memory_layer: tuple[str, ...]
    source_evidence_refs: tuple[str, ...]
    write_back_mode: str
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


def build_memory_writeback_request_v0(
    *,
    write_back_seed: str,
    subject_id: str,
    write_back_reason: tuple[str, ...] | list[str] = (),
    target_memory_layer: tuple[str, ...] | list[str] = (),
    source_evidence_refs: tuple[str, ...] | list[str] = (),
    write_back_mode: str,
) -> MemoryWriteBackRequestV0:
    if not write_back_seed.strip():
        raise ValueError("missing write_back_seed")
    if not subject_id.strip():
        raise ValueError("missing subject_id")
    if write_back_mode not in ALLOWED_WRITEBACK_MODES_V0:
        raise ValueError("unsupported write_back_mode")

    normalized_write_back_reason = normalize_str_tuple_v0(write_back_reason)
    normalized_target_memory_layer = normalize_str_tuple_v0(target_memory_layer)
    normalized_source_evidence_refs = normalize_str_tuple_v0(source_evidence_refs)

    for layer in normalized_target_memory_layer:
        if layer not in ALLOWED_TARGET_MEMORY_LAYERS_V0:
            raise ValueError("unsupported target_memory_layer")

    write_back_id = f"memory-writeback::{write_back_seed.strip()}"

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "write_back_id": write_back_id,
        "subject_id": subject_id.strip(),
        "write_back_mode": write_back_mode,
        "target_memory_layer_count": len(normalized_target_memory_layer),
        "source_evidence_ref_count": len(normalized_source_evidence_refs),
    }

    return MemoryWriteBackRequestV0(
        write_back_version=MEMORY_WRITEBACK_REQUEST_VERSION_V0,
        write_back_id=write_back_id,
        subject_id=subject_id.strip(),
        write_back_reason=normalized_write_back_reason,
        target_memory_layer=normalized_target_memory_layer,
        source_evidence_refs=normalized_source_evidence_refs,
        write_back_mode=write_back_mode,
        trace=trace,
    )


def memory_writeback_request_to_payload_v0(
    write_back_request: MemoryWriteBackRequestV0,
) -> dict[str, object]:
    return {
        "write_back_version": write_back_request.write_back_version,
        "write_back_id": write_back_request.write_back_id,
        "subject_id": write_back_request.subject_id,
        "write_back_reason": tuple(write_back_request.write_back_reason),
        "target_memory_layer": tuple(write_back_request.target_memory_layer),
        "source_evidence_refs": tuple(write_back_request.source_evidence_refs),
        "write_back_mode": write_back_request.write_back_mode,
        "trace": dict(write_back_request.trace),
    }


__all__ = [
    "ALLOWED_TARGET_MEMORY_LAYERS_V0",
    "ALLOWED_WRITEBACK_MODES_V0",
    "MEMORY_WRITEBACK_REQUEST_VERSION_V0",
    "MemoryWriteBackRequestV0",
    "build_memory_writeback_request_v0",
    "memory_writeback_request_to_payload_v0",
    "normalize_str_tuple_v0",
]
