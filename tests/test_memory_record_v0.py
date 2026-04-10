import pytest

from mmn.contracts.memory_record_v0 import build_memory_record_v0


def test_build_memory_record_v0_rejects_blank_record_seed() -> None:
    with pytest.raises(ValueError, match="missing record_seed"):
        build_memory_record_v0(
            record_seed="   ",
            record_kind="summary_note",
            record_text="alpha",
        )


def test_build_memory_record_v0_rejects_unsupported_record_kind() -> None:
    with pytest.raises(ValueError, match="unsupported record_kind"):
        build_memory_record_v0(
            record_seed="alpha",
            record_kind="unknown_note",
            record_text="alpha",
        )


def test_build_memory_record_v0_rejects_blank_record_text() -> None:
    with pytest.raises(ValueError, match="missing record_text"):
        build_memory_record_v0(
            record_seed="alpha",
            record_kind="summary_note",
            record_text="   ",
        )


def test_build_memory_record_v0_normalizes_text_and_reason_codes() -> None:
    record = build_memory_record_v0(
        record_seed="alpha",
        record_kind="summary_note",
        record_text="  alpha summary  ",
        reason_codes=[" A ", "", "B"],
    )

    assert record.record_text == "alpha summary"
    assert record.reason_codes == ("A", "B")
