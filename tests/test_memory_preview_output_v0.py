from dataclasses import asdict, fields

from mmn.contracts.memory_preview_output_v0 import build_memory_preview_output_v0
from mmn.contracts.memory_record_v0 import build_memory_record_v0


def test_memory_preview_output_shape_is_stable() -> None:
    note_record = build_memory_record_v0(
        record_seed="note",
        record_kind="summary_note",
        record_text="note text",
    )
    citation_record = build_memory_record_v0(
        record_seed="citation",
        record_kind="citation_note",
        record_text="citation text",
    )

    output = build_memory_preview_output_v0(
        output_seed="alpha",
        records=(note_record, citation_record),
        memory_strength_hint="medium",
        citation_hint="limited",
        reason_codes=("MEMORY_STUB",),
    )

    field_names = tuple(field.name for field in fields(output))
    assert field_names == (
        "memory_output_version",
        "memory_output_model_version",
        "memory_output_id",
        "records",
        "memory_strength_hint",
        "citation_hint",
        "reason_codes",
        "trace",
    )

    payload = asdict(output)
    assert payload["memory_output_version"] == "memory_preview_output_v0"
    assert payload["memory_output_id"] == "memory-preview::alpha"
