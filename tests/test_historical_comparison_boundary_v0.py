from __future__ import annotations

import pytest

from mmn.contracts.historical_comparison_object_v0 import (
    build_historical_comparison_object_v0,
)


def test_historical_comparison_rejects_empty_seed() -> None:
    with pytest.raises(ValueError):
        build_historical_comparison_object_v0(
            comparison_seed="",
            subject_id="subject-alpha",
            current_pattern_summary="single asset confirmation signal",
            comparison_confidence="low",
        )


def test_historical_comparison_rejects_empty_subject_id() -> None:
    with pytest.raises(ValueError):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="",
            current_pattern_summary="single asset confirmation signal",
            comparison_confidence="low",
        )


def test_historical_comparison_rejects_empty_pattern_summary() -> None:
    with pytest.raises(ValueError):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="subject-alpha",
            current_pattern_summary="",
            comparison_confidence="low",
        )


def test_historical_comparison_rejects_invalid_confidence() -> None:
    with pytest.raises(ValueError):
        build_historical_comparison_object_v0(
            comparison_seed="alpha",
            subject_id="subject-alpha",
            current_pattern_summary="single asset confirmation signal",
            comparison_confidence="invalid_confidence",
        )


def test_historical_comparison_builds_minimal_valid_object() -> None:
    obj = build_historical_comparison_object_v0(
        comparison_seed="alpha",
        subject_id="subject-alpha",
        current_pattern_summary="single asset confirmation signal",
        comparison_confidence="low",
    )

    assert obj.comparison_id == "historical-comparison::alpha"
    assert obj.subject_id == "subject-alpha"
    assert obj.current_pattern_summary == "single asset confirmation signal"
    assert obj.historical_pattern_refs == ()
    assert obj.matched_dimensions == ()
    assert obj.divergent_dimensions == ()
    assert obj.comparison_confidence == "low"
    assert obj.comparison_notes == ""

    assert obj.trace["source_stage"] == "historical_comparison_object_v0"
    assert obj.trace["comparison_id"] == "historical-comparison::alpha"
    assert obj.trace["subject_id"] == "subject-alpha"
    assert obj.trace["comparison_confidence"] == "low"
    assert obj.trace["historical_pattern_ref_count"] == 0


def test_historical_comparison_builds_richer_valid_object() -> None:
    obj = build_historical_comparison_object_v0(
        comparison_seed="beta",
        subject_id="subject-beta",
        current_pattern_summary="earnings upgrade with chain narrative",
        historical_pattern_refs=("hist-001", "hist-002"),
        matched_dimensions=("profit_growth", "upgrade_expectation"),
        divergent_dimensions=("chain_realization_weaker",),
        comparison_confidence="medium",
        comparison_notes="core asset resembles prior cases more than chain spread does",
    )

    assert obj.comparison_id == "historical-comparison::beta"
    assert obj.subject_id == "subject-beta"
    assert obj.current_pattern_summary == "earnings upgrade with chain narrative"
    assert obj.historical_pattern_refs == ("hist-001", "hist-002")
    assert obj.matched_dimensions == ("profit_growth", "upgrade_expectation")
    assert obj.divergent_dimensions == ("chain_realization_weaker",)
    assert obj.comparison_confidence == "medium"
    assert obj.comparison_notes == ("core asset resembles prior cases more than chain spread does")

    assert obj.trace["source_stage"] == "historical_comparison_object_v0"
    assert obj.trace["comparison_id"] == "historical-comparison::beta"
    assert obj.trace["subject_id"] == "subject-beta"
    assert obj.trace["comparison_confidence"] == "medium"
    assert obj.trace["historical_pattern_ref_count"] == 2
