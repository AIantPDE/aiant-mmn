from dataclasses import asdict, fields

from mmn.contracts.memory_record_v0 import build_memory_record_v0


def test_memory_record_shape_is_stable() -> None:
    record = build_memory_record_v0(
        record_seed="alpha",
        record_kind="summary_note",
        record_text="alpha summary",
        reason_codes=("MEMORY_STUB",),
    )

    field_names = tuple(field.name for field in fields(record))
    assert field_names == (
        "record_version",
        "record_id",
        "record_kind",
        "record_text",
        "reason_codes",
        "trace",
    )

    payload = asdict(record)
    assert payload["record_version"] == "memory_record_v0"
    assert payload["record_id"] == "memory-record::alpha"
