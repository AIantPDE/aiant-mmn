from __future__ import annotations

from collections.abc import Mapping
from dataclasses import dataclass

POSTERIOR_CORRECTION_VERSION_V0 = "posterior_correction_object_v0"
SOURCE_STAGE_V0 = "posterior_correction_object_v0"

ALLOWED_CORRECTION_DIRECTION_V0: tuple[str, ...] = (
    "up",
    "down",
    "neutral",
)

ALLOWED_CORRECTION_STRENGTH_V0: tuple[str, ...] = (
    "light",
    "medium",
    "strong",
)


@dataclass(frozen=True)
class PosteriorCorrectionObjectV0:
    correction_version: str
    correction_id: str
    subject_id: str
    correction_target: tuple[str, ...]
    correction_direction: str
    correction_strength: str
    correction_basis: tuple[str, ...]
    posterior_notes: str
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


def build_posterior_correction_object_v0(
    *,
    correction_seed: str,
    subject_id: str,
    correction_target: tuple[str, ...] | list[str] = (),
    correction_direction: str,
    correction_strength: str,
    correction_basis: tuple[str, ...] | list[str] = (),
    posterior_notes: str = "",
) -> PosteriorCorrectionObjectV0:
    if not correction_seed.strip():
        raise ValueError("missing correction_seed")
    if not subject_id.strip():
        raise ValueError("missing subject_id")
    if correction_direction not in ALLOWED_CORRECTION_DIRECTION_V0:
        raise ValueError("unsupported correction_direction")
    if correction_strength not in ALLOWED_CORRECTION_STRENGTH_V0:
        raise ValueError("unsupported correction_strength")

    correction_id = f"posterior-correction::{correction_seed.strip()}"
    normalized_correction_target = normalize_str_tuple_v0(correction_target)
    normalized_correction_basis = normalize_str_tuple_v0(correction_basis)

    trace: dict[str, object] = {
        "source_stage": SOURCE_STAGE_V0,
        "correction_id": correction_id,
        "subject_id": subject_id.strip(),
        "correction_direction": correction_direction,
        "correction_strength": correction_strength,
        "correction_basis_count": len(normalized_correction_basis),
    }

    return PosteriorCorrectionObjectV0(
        correction_version=POSTERIOR_CORRECTION_VERSION_V0,
        correction_id=correction_id,
        subject_id=subject_id.strip(),
        correction_target=normalized_correction_target,
        correction_direction=correction_direction,
        correction_strength=correction_strength,
        correction_basis=normalized_correction_basis,
        posterior_notes=posterior_notes.strip(),
        trace=trace,
    )


def posterior_correction_object_to_payload_v0(
    correction: PosteriorCorrectionObjectV0,
) -> dict[str, object]:
    return {
        "correction_version": correction.correction_version,
        "correction_id": correction.correction_id,
        "subject_id": correction.subject_id,
        "correction_target": tuple(correction.correction_target),
        "correction_direction": correction.correction_direction,
        "correction_strength": correction.correction_strength,
        "correction_basis": tuple(correction.correction_basis),
        "posterior_notes": correction.posterior_notes,
        "trace": dict(correction.trace),
    }


__all__ = [
    "ALLOWED_CORRECTION_DIRECTION_V0",
    "ALLOWED_CORRECTION_STRENGTH_V0",
    "POSTERIOR_CORRECTION_VERSION_V0",
    "PosteriorCorrectionObjectV0",
    "build_posterior_correction_object_v0",
    "posterior_correction_object_to_payload_v0",
    "normalize_str_tuple_v0",
]
