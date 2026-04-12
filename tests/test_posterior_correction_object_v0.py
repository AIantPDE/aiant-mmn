from dataclasses import asdict, fields

import pytest

from mmn.contracts.posterior_correction_object_v0 import (
    build_posterior_correction_object_v0,
    posterior_correction_object_to_payload_v0,
)


def test_posterior_correction_object_shape_is_stable() -> None:
    correction = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id="subject-alpha",
        correction_target=("core_asset_promotion_confidence",),
        correction_direction="down",
        correction_strength="medium",
        correction_basis=("historical_chain_sync_realization_low",),
        posterior_notes="chain spread should be discounted relative to core asset",
    )

    field_names = tuple(field.name for field in fields(correction))
    assert field_names == (
        "correction_version",
        "correction_id",
        "subject_id",
        "correction_target",
        "correction_direction",
        "correction_strength",
        "correction_basis",
        "posterior_notes",
        "trace",
    )

    payload = asdict(correction)
    assert payload["correction_version"] == "posterior_correction_object_v0"
    assert payload["correction_id"] == "posterior-correction::alpha"


def test_build_posterior_correction_object_v0_rejects_blank_correction_seed() -> None:
    with pytest.raises(ValueError, match="missing correction_seed"):
        build_posterior_correction_object_v0(
            correction_seed="   ",
            subject_id="subject-alpha",
            correction_direction="down",
            correction_strength="medium",
        )


def test_build_posterior_correction_object_v0_rejects_blank_subject_id() -> None:
    with pytest.raises(ValueError, match="missing subject_id"):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="   ",
            correction_direction="down",
            correction_strength="medium",
        )


def test_build_posterior_correction_object_v0_rejects_unsupported_correction_direction() -> None:
    with pytest.raises(ValueError, match="unsupported correction_direction"):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="subject-alpha",
            correction_direction="raise",
            correction_strength="medium",
        )


def test_build_posterior_correction_object_v0_rejects_unsupported_correction_strength() -> None:
    with pytest.raises(ValueError, match="unsupported correction_strength"):
        build_posterior_correction_object_v0(
            correction_seed="alpha",
            subject_id="subject-alpha",
            correction_direction="down",
            correction_strength="ultra",
        )


def test_build_posterior_correction_object_v0_normalizes_tuple_fields() -> None:
    correction = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id=" subject-alpha ",
        correction_target=[" core_asset ", "", "chain_spread"],
        correction_direction="down",
        correction_strength="strong",
        correction_basis=[" historical_chain_sync_realization_low ", "", "source_optimism_bias"],
        posterior_notes=" correction note ",
    )

    assert correction.subject_id == "subject-alpha"
    assert correction.correction_target == ("core_asset", "chain_spread")
    assert correction.correction_basis == (
        "historical_chain_sync_realization_low",
        "source_optimism_bias",
    )
    assert correction.posterior_notes == "correction note"


def test_posterior_correction_object_payload_projection_is_stable() -> None:
    correction = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id="subject-alpha",
        correction_target=("core_asset_promotion_confidence",),
        correction_direction="down",
        correction_strength="medium",
        correction_basis=("historical_chain_sync_realization_low",),
        posterior_notes="chain spread should be discounted relative to core asset",
    )

    payload = posterior_correction_object_to_payload_v0(correction)

    assert payload == {
        "correction_version": "posterior_correction_object_v0",
        "correction_id": "posterior-correction::alpha",
        "subject_id": "subject-alpha",
        "correction_target": ("core_asset_promotion_confidence",),
        "correction_direction": "down",
        "correction_strength": "medium",
        "correction_basis": ("historical_chain_sync_realization_low",),
        "posterior_notes": "chain spread should be discounted relative to core asset",
        "trace": {
            "source_stage": "posterior_correction_object_v0",
            "correction_id": "posterior-correction::alpha",
            "subject_id": "subject-alpha",
            "correction_direction": "down",
            "correction_strength": "medium",
            "correction_basis_count": 1,
        },
    }
