from dataclasses import asdict, fields

import pytest

from mmn.contracts.historical_comparison_object_v0 import (
    build_historical_comparison_object_v0,
    historical_comparison_object_to_payload_v0,
)


def test_historical_comparison_object_shape_is_stable() -> None:
    comparison = build_historical_comparison_object_v0(
        comparison_seed="alpha",
        subject_id="subject-alpha",
        current_pattern_summary="earnings upgrade with chain narrative",
        historical_pattern_refs=("hist-001", "hist-002"),
        matched_dimensions=("profit_growth", "upgrade_expectation"),
        divergent_dimensions=("chain_realization_weaker",),
        comparison_confidence="medium",
        comparison_notes="core asset resembles prior cases more than chain spread does",
    )

    field_names = tuple(field.name for field in fields(comparison))
    assert field_names == (
        "comparison_version",
        "comparison_id",
        "subject_id",
        "current_pattern_summary",
        "historical_pattern_refs",
        "matched_dimensions",
        "divergent_dimensions",
        "comparison_confidence",
        "comparison_notes",
        "trace",
    )

    payload = asdict(comparison)
    assert payload["comparison_version"] == "historical_comparison_object_v0"
    assert payload["comparison_id"] == "historical-comparison::alpha"


def test_build_historical_comparison_object_v0_rejects_blank_comparison_seed() -> None:
    with pytest.raises(ValueError, match="missing comparison_seed"):
        build_historical_comparison_object_v0(
            comparison_seed="   ",
            subject_id="subject-alpha",
            current_pattern_summary="pattern",
            comparison_confidence="medium",
        )


def test_build_historical_comparison_object_v0_rejects_blank_subject_id() -> None:
    with pytest.raises(ValueError, match="missing subject_id"):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="   ",
            current_pattern_summary="pattern",
            comparison_confidence="medium",
        )


def test_build_historical_comparison_object_v0_rejects_blank_current_pattern_summary() -> None:
    with pytest.raises(ValueError, match="missing current_pattern_summary"):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="subject-alpha",
            current_pattern_summary="   ",
            comparison_confidence="medium",
        )


def test_build_historical_comparison_object_v0_rejects_unsupported_comparison_confidence() -> None:
    with pytest.raises(ValueError, match="unsupported comparison_confidence"):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="subject-alpha",
            current_pattern_summary="pattern",
            comparison_confidence="ultra",
        )


def test_build_historical_comparison_object_v0_normalizes_tuple_fields() -> None:
    comparison = build_historical_comparison_object_v0(
        comparison_seed="alpha",
        subject_id=" subject-alpha ",
        current_pattern_summary=" pattern ",
        historical_pattern_refs=[" hist-001 ", "", "hist-002"],
        matched_dimensions=[" fact_signal ", "", "upgrade_hint"],
        divergent_dimensions=[" chain_uncertain "],
        comparison_confidence="high",
        comparison_notes=" comparison note ",
    )

    assert comparison.subject_id == "subject-alpha"
    assert comparison.current_pattern_summary == "pattern"
    assert comparison.historical_pattern_refs == ("hist-001", "hist-002")
    assert comparison.matched_dimensions == ("fact_signal", "upgrade_hint")
    assert comparison.divergent_dimensions == ("chain_uncertain",)
    assert comparison.comparison_notes == "comparison note"


def test_historical_comparison_object_payload_projection_is_stable() -> None:
    comparison = build_historical_comparison_object_v0(
        comparison_seed="alpha",
        subject_id="subject-alpha",
        current_pattern_summary="earnings upgrade with chain narrative",
        historical_pattern_refs=("hist-001", "hist-002"),
        matched_dimensions=("profit_growth", "upgrade_expectation"),
        divergent_dimensions=("chain_realization_weaker",),
        comparison_confidence="medium",
        comparison_notes="core asset resembles prior cases more than chain spread does",
    )

    payload = historical_comparison_object_to_payload_v0(comparison)

    assert payload == {
        "comparison_version": "historical_comparison_object_v0",
        "comparison_id": "historical-comparison::alpha",
        "subject_id": "subject-alpha",
        "current_pattern_summary": "earnings upgrade with chain narrative",
        "historical_pattern_refs": ("hist-001", "hist-002"),
        "matched_dimensions": ("profit_growth", "upgrade_expectation"),
        "divergent_dimensions": ("chain_realization_weaker",),
        "comparison_confidence": "medium",
        "comparison_notes": "core asset resembles prior cases more than chain spread does",
        "trace": {
            "source_stage": "historical_comparison_object_v0",
            "comparison_id": "historical-comparison::alpha",
            "subject_id": "subject-alpha",
            "comparison_confidence": "medium",
            "historical_pattern_ref_count": 2,
        },
    }
