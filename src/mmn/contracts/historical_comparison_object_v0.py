from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

HISTORICAL_COMPARISON_VERSION_V0 = "historical_comparison_object_v0"
SOURCE_STAGE_V0 = "historical_comparison_object_v0"

ALLOWED_COMPARISON_CONFIDENCE_V0: tuple[str, ...] = (
    "low",
    "medium",
    "high",
)


@dataclass(frozen=True)
class HistoricalComparisonObjectV0:
    comparison_version: str
    comparison_id: str
    subject_id: str
    current_pattern_summary: str
    historical_pattern_refs: tuple[str, ...]
    matched_dimensions: tuple[str, ...]
    divergent_dimensions: tuple[str, ...]
    comparison_confidence: str
    comparison_notes: str
    trace: Mapping[str, object]


def normalize_str_tuple_v0(value: object) -> tuple[str, ...]:
    if value is None:
        return ()
    if isinstance(value, str):
        item = value.strip()
        return (item,) if item else ()

    normalized: list[str] = []
    try:
        for item in value:  # type: ignore[assignment]
            if isinstance(item, str):
                stripped = item.strip()
                if stripped:
                    normalized.append(stripped)
    except TypeError:
        return ()
    return tuple(normalized)


def build_historical_comparison_object_v0(
    *,
    comparison_seed: str,
    subject_id: str,
    current_pattern_summary: str,
    historical_pattern_refs: tuple[str, ...] | list[str] = (),
    matched_dimensions: tuple[str, ...] | list[str] = (),
    divergent_dimensions: tuple[str, ...] | list[str] = (),
    comparison_confidence: str,
    comparison_notes: str = "",
) -> HistoricalComparisonObjectV0:
    if not comparison_seed.strip():
        raise ValueError("missing comparison_seed")
    if not subject_id.strip():
        raise ValueError("missing subject_id")
    if not current_pattern_summary.strip():
        raise ValueError("missing current_pattern_summary")
    if comparison_confidence not in ALLOWED_COMPARISON_CONFIDENCE_V0:
        raise ValueError("unsupported comparison_confidence")

    comparison_id = f"historical-comparison::{comparison_seed.strip()}"
    normalized_historical_pattern_refs = normalize_str_tuple_v0(historical_pattern_refs)
    normalized_matched_dimensions = normalize_str_tuple_v0(matched_dimensions)
    normalized_divergent_dimensions = normalize_str_tuple_v0(divergent_dimensions)

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "comparison_id": comparison_id,
        "subject_id": subject_id.strip(),
        "comparison_confidence": comparison_confidence,
        "historical_pattern_ref_count": len(normalized_historical_pattern_refs),
    }

    return HistoricalComparisonObjectV0(
        comparison_version=HISTORICAL_COMPARISON_VERSION_V0,
        comparison_id=comparison_id,
        subject_id=subject_id.strip(),
        current_pattern_summary=current_pattern_summary.strip(),
        historical_pattern_refs=normalized_historical_pattern_refs,
        matched_dimensions=normalized_matched_dimensions,
        divergent_dimensions=normalized_divergent_dimensions,
        comparison_confidence=comparison_confidence,
        comparison_notes=comparison_notes.strip(),
        trace=trace,
    )


def historical_comparison_object_to_payload_v0(
    comparison: HistoricalComparisonObjectV0,
) -> dict[str, object]:
    return {
        "comparison_version": comparison.comparison_version,
        "comparison_id": comparison.comparison_id,
        "subject_id": comparison.subject_id,
        "current_pattern_summary": comparison.current_pattern_summary,
        "historical_pattern_refs": tuple(comparison.historical_pattern_refs),
        "matched_dimensions": tuple(comparison.matched_dimensions),
        "divergent_dimensions": tuple(comparison.divergent_dimensions),
        "comparison_confidence": comparison.comparison_confidence,
        "comparison_notes": comparison.comparison_notes,
        "trace": dict(comparison.trace),
    }


__all__ = [
    "ALLOWED_COMPARISON_CONFIDENCE_V0",
    "HISTORICAL_COMPARISON_VERSION_V0",
    "HistoricalComparisonObjectV0",
    "build_historical_comparison_object_v0",
    "historical_comparison_object_to_payload_v0",
    "normalize_str_tuple_v0",
]
