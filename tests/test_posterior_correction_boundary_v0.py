from __future__ import annotations

import pytest

from mmn.contracts.posterior_correction_object_v0 import (
    build_posterior_correction_object_v0,
)


def test_posterior_correction_rejects_empty_seed() -> None:
    with pytest.raises(ValueError):
        build_posterior_correction_object_v0(
            correction_seed="",
            subject_id="subject-alpha",
            correction_direction="neutral",
            correction_strength="light",
        )


def test_posterior_correction_rejects_empty_subject_id() -> None:
    with pytest.raises(ValueError):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="",
            correction_direction="neutral",
            correction_strength="light",
        )


def test_posterior_correction_rejects_invalid_direction() -> None:
    with pytest.raises(ValueError):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="subject-alpha",
            correction_direction="invalid_direction",
            correction_strength="light",
        )


def test_posterior_correction_rejects_invalid_strength() -> None:
    with pytest.raises(ValueError):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="subject-alpha",
            correction_direction="neutral",
            correction_strength="invalid_strength",
        )


def test_posterior_correction_builds_minimal_valid_object() -> None:
    obj = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id="subject-alpha",
        correction_direction="neutral",
        correction_strength="light",
    )

    assert obj.correction_id == "posterior-correction::alpha"
    assert obj.subject_id == "subject-alpha"
    assert obj.correction_target == ()
    assert obj.correction_direction == "neutral"
    assert obj.correction_strength == "light"
    assert obj.correction_basis == ()
    assert obj.posterior_notes == ""

    assert obj.trace["source_stage"] == "posterior_correction_object_v0"
    assert obj.trace["correction_id"] == "posterior-correction::alpha"
    assert obj.trace["subject_id"] == "subject-alpha"
    assert obj.trace["correction_direction"] == "neutral"
    assert obj.trace["correction_strength"] == "light"
    assert obj.trace["correction_basis_count"] == 0


def test_posterior_correction_builds_richer_valid_object() -> None:
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

    assert obj.correction_id == "posterior-correction::beta"
    assert obj.subject_id == "subject-beta"
    assert obj.correction_target == (
        "core_asset_promotion_confidence",
        "chain_spread_expectation",
    )
    assert obj.correction_direction == "down"
    assert obj.correction_strength == "medium"
    assert obj.correction_basis == (
        "historical-comparison::beta",
        "historical_chain_sync_realization_low",
    )
    assert obj.posterior_notes == ("chain spread should be discounted relative to core asset")

    assert obj.trace["source_stage"] == "posterior_correction_object_v0"
    assert obj.trace["correction_id"] == "posterior-correction::beta"
    assert obj.trace["subject_id"] == "subject-beta"
    assert obj.trace["correction_direction"] == "down"
    assert obj.trace["correction_strength"] == "medium"
    assert obj.trace["correction_basis_count"] == 2
