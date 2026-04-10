import pytest

from mmn.contracts.memory_preview_output_v0 import build_memory_preview_output_v0
from mmn.contracts.memory_record_v0 import build_memory_record_v0


def _build_record():
    return build_memory_record_v0(
        record_seed="note",
        record_kind="summary_note",
        record_text="note text",
    )


def test_build_memory_preview_output_v0_rejects_blank_output_seed() -> None:
    with pytest.raises(ValueError, match="missing output_seed"):
        build_memory_preview_output_v0(
            output_seed="   ",
            records=(_build_record(),),
            memory_strength_hint="medium",
            citation_hint="limited",
        )


def test_build_memory_preview_output_v0_rejects_unsupported_memory_strength_hint() -> None:
    with pytest.raises(ValueError, match="unsupported memory_strength_hint"):
        build_memory_preview_output_v0(
            output_seed="alpha",
            records=(_build_record(),),
            memory_strength_hint="ultra",
            citation_hint="limited",
        )


def test_build_memory_preview_output_v0_rejects_unsupported_citation_hint() -> None:
    with pytest.raises(ValueError, match="unsupported citation_hint"):
        build_memory_preview_output_v0(
            output_seed="alpha",
            records=(_build_record(),),
            memory_strength_hint="medium",
            citation_hint="full",
        )


def test_build_memory_preview_output_v0_normalizes_reason_codes() -> None:
    output = build_memory_preview_output_v0(
        output_seed="alpha",
        records=(_build_record(),),
        memory_strength_hint="medium",
        citation_hint="limited",
        reason_codes=[" A ", "", "B"],
    )

    assert output.reason_codes == ("A", "B")


def test_build_memory_preview_output_v0_converts_records_to_tuple() -> None:
    output = build_memory_preview_output_v0(
        output_seed="alpha",
        records=[_build_record()],
        memory_strength_hint="medium",
        citation_hint="limited",
    )

    assert isinstance(output.records, tuple)
    assert len(output.records) == 1
