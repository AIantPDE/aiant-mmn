from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

MEMORY_WRITEBACK_PREVIEW_VERSION_V0 = "memory_writeback_preview_v0"
SOURCE_STAGE_V0 = "memory_writeback_preview_v0"
PREVIEW_STATE_V0 = "reference_only_preview"

FORBIDDEN_EXECUTION_FIELDS_V0: frozenset[str] = frozenset(
    {
        "dmf_bootstrap",
        "execution_payload",
        "fetch_command",
        "memory_write_authorized",
        "model_call",
        "persistent_memory_mutation_authorized",
        "provider_backend_call",
        "queue_mutation",
        "route_decision",
        "runtime_authority_granted",
        "scheduler_apply",
        "shared_contract_expansion",
        "worker_dispatch",
    }
)


@dataclass(frozen=True)
class MemoryWritebackPreviewV0:
    preview_version: str
    preview_id: str
    source_memory_output_id: str
    preview_state: str
    reason_codes: tuple[str, ...]
    evidence_refs: tuple[str, ...]
    memory_write_authorized: bool
    persistent_memory_mutation_authorized: bool
    runtime_authority_granted: bool
    trace: Mapping[str, object]


def normalize_str_tuple_v0(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        item = value.strip()
        return (item,) if item else ()
    if not isinstance(value, (list, tuple)):
        raise ValueError("value must be a string, list, tuple, or None")

    normalized: list[str] = []
    for item in value:
        if not isinstance(item, str):
            raise ValueError("value items must be strings")
        stripped = item.strip()
        if stripped and stripped not in normalized:
            normalized.append(stripped)
    return tuple(normalized)


def build_memory_writeback_preview_v0(
    *,
    preview_seed: str,
    source_memory_output_id: str,
    reason_codes: tuple[str, ...] | list[str] = (),
    evidence_refs: tuple[str, ...] | list[str] = (),
    material: Mapping[str, object] | None = None,
) -> MemoryWritebackPreviewV0:
    if not preview_seed.strip():
        raise ValueError("missing preview_seed")
    if not source_memory_output_id.strip():
        raise ValueError("missing source_memory_output_id")

    preview_material = dict(material or {})
    forbidden_present = sorted(FORBIDDEN_EXECUTION_FIELDS_V0.intersection(preview_material))
    if forbidden_present:
        raise ValueError("forbidden execution-like fields: " + ", ".join(forbidden_present))

    normalized_reason_codes = normalize_str_tuple_v0(reason_codes)
    normalized_evidence_refs = normalize_str_tuple_v0(evidence_refs)
    preview_id = f"memory-writeback-preview::{preview_seed.strip()}"

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "preview_id": preview_id,
        "source_memory_output_id": source_memory_output_id.strip(),
        "preview_state": PREVIEW_STATE_V0,
        "reason_codes": normalized_reason_codes,
        "evidence_refs": normalized_evidence_refs,
        "memory_write_authorized": False,
        "persistent_memory_mutation_authorized": False,
        "runtime_authority_granted": False,
    }

    return MemoryWritebackPreviewV0(
        preview_version=MEMORY_WRITEBACK_PREVIEW_VERSION_V0,
        preview_id=preview_id,
        source_memory_output_id=source_memory_output_id.strip(),
        preview_state=PREVIEW_STATE_V0,
        reason_codes=normalized_reason_codes,
        evidence_refs=normalized_evidence_refs,
        memory_write_authorized=False,
        persistent_memory_mutation_authorized=False,
        runtime_authority_granted=False,
        trace=trace,
    )


def memory_writeback_preview_to_payload_v0(
    preview: MemoryWritebackPreviewV0,
) -> dict[str, object]:
    return {
        "preview_version": preview.preview_version,
        "preview_id": preview.preview_id,
        "source_memory_output_id": preview.source_memory_output_id,
        "preview_state": preview.preview_state,
        "reason_codes": tuple(preview.reason_codes),
        "evidence_refs": tuple(preview.evidence_refs),
        "memory_write_authorized": preview.memory_write_authorized,
        "persistent_memory_mutation_authorized": (preview.persistent_memory_mutation_authorized),
        "runtime_authority_granted": preview.runtime_authority_granted,
        "trace": dict(preview.trace),
    }


__all__ = [
    "FORBIDDEN_EXECUTION_FIELDS_V0",
    "MEMORY_WRITEBACK_PREVIEW_VERSION_V0",
    "MemoryWritebackPreviewV0",
    "build_memory_writeback_preview_v0",
    "memory_writeback_preview_to_payload_v0",
    "normalize_str_tuple_v0",
]
