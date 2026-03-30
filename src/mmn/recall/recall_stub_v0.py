from __future__ import annotations

from collections.abc import Mapping


def build_recall_stub_v0(memory_output: Mapping[str, object]) -> dict[str, object]:
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

    recall_state = (
        "memory_recall_preferred" if citation_hint == "available" else "memory_recall_observe"
    )

    return {
        "recall_version": "recall_stub_v0",
        "recall_id": f"memory-recall::{memory_output_id}",
        "memory_output_id": memory_output_id,
        "recall_state": recall_state,
        "reason_codes": tuple(memory_output.get("reason_codes", ())),
        "trace": {
            "source_stage": "recall_stub_v0",
            "memory_output_id": memory_output_id,
            "memory_strength_hint": memory_strength_hint.strip(),
            "citation_hint": citation_hint.strip(),
            "recall_state": recall_state,
        },
    }
