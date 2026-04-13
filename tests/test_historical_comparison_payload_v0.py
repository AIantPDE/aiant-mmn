from __future__ import annotations

from typing import cast

from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.historical_comparison_object_v0 import (
    build_historical_comparison_object_v0,
    historical_comparison_object_to_payload_v0,
)


def test_historical_comparison_payload_v0_minimal_projection() -> None:
    obj = build_historical_comparison_object_v0(
        comparison_seed="alpha",
        subject_id="subject-alpha",
        current_pattern_summary="single asset confirmation signal",
        comparison_confidence="low",
    )

    payload = cast(dict[str, object], historical_comparison_object_to_payload_v0(obj))

    assert payload["comparison_version"] == "historical_comparison_object_v0"
    assert payload["comparison_id"] == "historical-comparison::alpha"
    assert payload["subject_id"] == "subject-alpha"
    assert payload["current_pattern_summary"] == "single asset confirmation signal"
    assert payload["historical_pattern_refs"] == ()
    assert payload["matched_dimensions"] == ()
    assert payload["divergent_dimensions"] == ()
    assert payload["comparison_confidence"] == "low"
    assert payload["comparison_notes"] == ""

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "historical_comparison_object_v0"
    assert trace["comparison_id"] == "historical-comparison::alpha"
    assert trace["subject_id"] == "subject-alpha"
    assert trace["comparison_confidence"] == "low"
    assert trace["historical_pattern_ref_count"] == 0

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_historical_comparison_payload_v0_richer_projection() -> None:
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

    payload = cast(dict[str, object], historical_comparison_object_to_payload_v0(obj))

    assert payload["comparison_version"] == "historical_comparison_object_v0"
    assert payload["comparison_id"] == "historical-comparison::beta"
    assert payload["subject_id"] == "subject-beta"
    assert payload["current_pattern_summary"] == "earnings upgrade with chain narrative"
    assert payload["historical_pattern_refs"] == ("hist-001", "hist-002")
    assert payload["matched_dimensions"] == ("profit_growth", "upgrade_expectation")
    assert payload["divergent_dimensions"] == ("chain_realization_weaker",)
    assert payload["comparison_confidence"] == "medium"
    assert payload["comparison_notes"] == (
        "core asset resembles prior cases more than chain spread does"
    )

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "historical_comparison_object_v0"
    assert trace["comparison_id"] == "historical-comparison::beta"
    assert trace["subject_id"] == "subject-beta"
    assert trace["comparison_confidence"] == "medium"
    assert trace["historical_pattern_ref_count"] == 2

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_historical_comparison_payload_v0_trace_matches_normalized_refs() -> None:
    obj = build_historical_comparison_object_v0(
        comparison_seed="gamma",
        subject_id="subject-gamma",
        current_pattern_summary="gamma pattern",
        historical_pattern_refs=("hist-001", "hist-001", "hist-002"),
        matched_dimensions=("profit_growth", "profit_growth"),
        divergent_dimensions=("lagged_chain", "lagged_chain"),
        comparison_confidence="high",
    )

    payload = cast(dict[str, object], historical_comparison_object_to_payload_v0(obj))
    trace = cast(dict[str, object], payload["trace"])
    historical_pattern_refs = cast(tuple[str, ...], payload["historical_pattern_refs"])

    assert trace["source_stage"] == "historical_comparison_object_v0"
    assert trace["historical_pattern_ref_count"] == len(historical_pattern_refs)

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload
