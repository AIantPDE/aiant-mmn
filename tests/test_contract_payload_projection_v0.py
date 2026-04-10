from mmn.contracts.memory_preview_output_v0 import (
    build_memory_preview_output_v0,
    memory_preview_output_to_payload_v0,
)
from mmn.contracts.memory_record_v0 import (
    build_memory_record_v0,
    memory_record_to_payload_v0,
)


def test_memory_record_payload_projection_is_stable() -> None:
    record = build_memory_record_v0(
        record_seed="alpha",
        record_kind="summary_note",
        record_text="alpha summary",
        reason_codes=("MEMORY_STUB",),
    )

    payload = memory_record_to_payload_v0(record)

    assert payload == {
        "record_version": "memory_record_v0",
        "record_id": "memory-record::alpha",
        "record_kind": "summary_note",
        "record_text": "alpha summary",
        "reason_codes": ("MEMORY_STUB",),
        "trace": {
            "source_stage": "memory_record_v0",
            "record_id": "memory-record::alpha",
            "record_kind": "summary_note",
            "record_text": "alpha summary",
            "reason_codes": ("MEMORY_STUB",),
        },
    }


def test_memory_preview_output_payload_projection_is_stable() -> None:
    note_record = build_memory_record_v0(
        record_seed="note",
        record_kind="summary_note",
        record_text="note text",
        reason_codes=("MEMORY_STUB",),
    )
    citation_record = build_memory_record_v0(
        record_seed="citation",
        record_kind="citation_note",
        record_text="citation text",
        reason_codes=("MEMORY_STUB",),
    )

    output = build_memory_preview_output_v0(
        output_seed="alpha",
        records=(note_record, citation_record),
        memory_strength_hint="medium",
        citation_hint="limited",
        reason_codes=("MEMORY_STUB",),
    )

    payload = memory_preview_output_to_payload_v0(output)

    assert payload["memory_output_version"] == "memory_preview_output_v0"
    assert payload["memory_output_model_version"] == "memory_preview_output_model_v0"
    assert payload["memory_output_id"] == "memory-preview::alpha"
    assert payload["memory_strength_hint"] == "medium"
    assert payload["citation_hint"] == "limited"
    assert payload["reason_codes"] == ("MEMORY_STUB",)
    assert payload["trace"] == {
        "source_stage": "memory_preview_output_v0",
        "memory_output_id": "memory-preview::alpha",
        "record_count": 2,
        "memory_strength_hint": "medium",
        "citation_hint": "limited",
        "reason_codes": ("MEMORY_STUB",),
    }

    assert payload["records"] == (
        {
            "record_version": "memory_record_v0",
            "record_id": "memory-record::note",
            "record_kind": "summary_note",
            "record_text": "note text",
            "reason_codes": ("MEMORY_STUB",),
            "trace": {
                "source_stage": "memory_record_v0",
                "record_id": "memory-record::note",
                "record_kind": "summary_note",
                "record_text": "note text",
                "reason_codes": ("MEMORY_STUB",),
            },
        },
        {
            "record_version": "memory_record_v0",
            "record_id": "memory-record::citation",
            "record_kind": "citation_note",
            "record_text": "citation text",
            "reason_codes": ("MEMORY_STUB",),
            "trace": {
                "source_stage": "memory_record_v0",
                "record_id": "memory-record::citation",
                "record_kind": "citation_note",
                "record_text": "citation text",
                "reason_codes": ("MEMORY_STUB",),
            },
        },
    )
