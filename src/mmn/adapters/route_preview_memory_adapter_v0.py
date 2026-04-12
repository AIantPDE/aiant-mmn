from __future__ import annotations

from collections.abc import Mapping

from mmn.contracts.memory_preview_output_v0 import normalize_str_tuple_v0

FORBIDDEN_EXECUTION_FIELDS_V0: tuple[str, ...] = (
    "task_id",
    "job_name",
    "queue_name",
    "worker_target",
    "execution_payload",
    "backend_write_plan",
    "job_type",
    "dispatch_target",
    "dispatch_plan",
    "table_name",
    "table_write",
    "db_write",
)


def adapt_memory_preview_for_route_preview_v0(
    memory_output: Mapping[str, object],
) -> dict[str, object]:
    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        if field_name in memory_output:
            raise ValueError(
                f"memory preview adapter blocked forbidden execution field: {field_name}"
            )

    memory_output_version = memory_output.get("memory_output_version")
    if memory_output_version != "memory_preview_output_v0":
        raise ValueError("unsupported memory output version")

    memory_output_id = memory_output.get("memory_output_id")
    if not isinstance(memory_output_id, str) or not memory_output_id.strip():
        raise ValueError("missing memory_output_id")

    memory_strength_hint = memory_output.get("memory_strength_hint")
    citation_hint = memory_output.get("citation_hint")

    if not isinstance(memory_strength_hint, str) or not memory_strength_hint.strip():
        raise ValueError("missing memory_strength_hint")
    if not isinstance(citation_hint, str) or not citation_hint.strip():
        raise ValueError("missing citation_hint")

    normalized_reason_codes = normalize_str_tuple_v0(memory_output.get("reason_codes", ()))

    return {
        "memory_semantic_input_version": "route_preview_memory_input_v0",
        "memory_semantic_input_id": f"route-preview-memory::{memory_output_id}",
        "memory_output_id": memory_output_id,
        "memory_strength_hint": memory_strength_hint.strip(),
        "citation_hint": citation_hint.strip(),
        "reason_codes": normalized_reason_codes,
        "trace": {
            "source_stage": "route_preview_memory_adapter_v0",
            "memory_output_id": memory_output_id,
            "memory_strength_hint": memory_strength_hint.strip(),
            "citation_hint": citation_hint.strip(),
        },
    }
