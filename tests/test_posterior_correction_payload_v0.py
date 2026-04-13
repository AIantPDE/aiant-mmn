from __future__ import annotations

from typing import cast

from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.posterior_correction_object_v0 import (
    build_posterior_correction_object_v0,
    posterior_correction_object_to_payload_v0,
)


def test_posterior_correction_payload_v0_minimal_projection() -> None:
    obj = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id="subject-alpha",
        correction_direction="neutral",
        correction_strength="light",
    )

    payload = cast(dict[str, object], posterior_correction_object_to_payload_v0(obj))

    assert payload["correction_version"] == "posterior_correction_object_v0"
    assert payload["correction_id"] == "posterior-correction::alpha"
    assert payload["subject_id"] == "subject-alpha"
    assert payload["correction_target"] == ()
    assert payload["correction_direction"] == "neutral"
    assert payload["correction_strength"] == "light"
    assert payload["correction_basis"] == ()
    assert payload["posterior_notes"] == ""

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "posterior_correction_object_v0"
    assert trace["correction_id"] == "posterior-correction::alpha"
    assert trace["subject_id"] == "subject-alpha"
    assert trace["correction_direction"] == "neutral"
    assert trace["correction_strength"] == "light"
    assert trace["correction_basis_count"] == 0

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_posterior_correction_payload_v0_richer_projection() -> None:
    obj = build_posterior_correction_object_v0(
        correction_seed="beta",
        subject_id="subject-beta",
        correction_target=("core_asset_promotion_confidence", "chain_spread_expectation"),
        correction_direction="down",
        correction_strength="medium",
        correction_basis=(
            "historical-comparison::beta",
            "historical_chain_sync_realization_low",
        ),
        posterior_notes="chain spread should be discounted relative to core asset",
    )

    payload = cast(dict[str, object], posterior_correction_object_to_payload_v0(obj))

    assert payload["correction_version"] == "posterior_correction_object_v0"
    assert payload["correction_id"] == "posterior-correction::beta"
    assert payload["subject_id"] == "subject-beta"
    assert payload["correction_target"] == (
        "core_asset_promotion_confidence",
        "chain_spread_expectation",
    )
    assert payload["correction_direction"] == "down"
    assert payload["correction_strength"] == "medium"
    assert payload["correction_basis"] == (
        "historical-comparison::beta",
        "historical_chain_sync_realization_low",
    )
    assert payload["posterior_notes"] == (
        "chain spread should be discounted relative to core asset"
    )

    trace = cast(dict[str, object], payload["trace"])
    assert trace["source_stage"] == "posterior_correction_object_v0"
    assert trace["correction_id"] == "posterior-correction::beta"
    assert trace["subject_id"] == "subject-beta"
    assert trace["correction_direction"] == "down"
    assert trace["correction_strength"] == "medium"
    assert trace["correction_basis_count"] == 2

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload


def test_posterior_correction_payload_v0_trace_matches_normalized_basis() -> None:
    obj = build_posterior_correction_object_v0(
        correction_seed="gamma",
        subject_id="subject-gamma",
        correction_target=("target-a", "target-a"),
        correction_direction="up",
        correction_strength="medium",
        correction_basis=("basis-1", "basis-1", "basis-2"),
        posterior_notes="gamma note",
    )

    payload = cast(dict[str, object], posterior_correction_object_to_payload_v0(obj))
    trace = cast(dict[str, object], payload["trace"])
    correction_basis = cast(tuple[str, ...], payload["correction_basis"])

    assert trace["source_stage"] == "posterior_correction_object_v0"
    assert trace["correction_basis_count"] == len(correction_basis)

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in payload
