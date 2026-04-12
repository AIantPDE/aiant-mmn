from mmn.adapters import FORBIDDEN_EXECUTION_FIELDS_V0
from mmn.contracts.historical_comparison_object_v0 import (
    build_historical_comparison_object_v0,
    historical_comparison_object_to_payload_v0,
)
from mmn.contracts.memory_writeback_record_v0 import (
    build_memory_writeback_record_v0,
    memory_writeback_record_to_payload_v0,
)
from mmn.contracts.memory_writeback_request_v0 import (
    build_memory_writeback_request_v0,
    memory_writeback_request_to_payload_v0,
)
from mmn.contracts.posterior_correction_object_v0 import (
    build_posterior_correction_object_v0,
    posterior_correction_object_to_payload_v0,
)


def test_mmn_object_chain_smoke_v0() -> None:
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

    correction = build_posterior_correction_object_v0(
        correction_seed="alpha",
        subject_id=comparison.subject_id,
        correction_target=("core_asset_promotion_confidence", "chain_spread_expectation"),
        correction_direction="down",
        correction_strength="medium",
        correction_basis=(
            comparison.comparison_id,
            "historical_chain_sync_realization_low",
        ),
        posterior_notes="chain spread should be discounted relative to core asset",
    )

    write_back_request = build_memory_writeback_request_v0(
        write_back_seed="alpha",
        subject_id=correction.subject_id,
        write_back_reason=(
            "posterior_update_required",
            "failed_chain_sync_exemplar",
        ),
        target_memory_layer=("posterior", "cold"),
        source_evidence_refs=(
            correction.correction_id,
            comparison.comparison_id,
            "outcome_trace_001",
        ),
        write_back_mode="structured_posterior_update",
    )

    write_back_record = build_memory_writeback_record_v0(
        write_back_seed="alpha",
        stored_memory_ref="mem_posterior_core_vs_chain_lag_003",
        stored_memory_layer="posterior",
        stored_memory_kind="propagation_realization_correction",
        write_back_status="stored",
        retention_hint="long_term",
        write_back_notes="core asset tends to realize earlier than chain spread",
    )

    comparison_payload = historical_comparison_object_to_payload_v0(comparison)
    correction_payload = posterior_correction_object_to_payload_v0(correction)
    write_back_request_payload = memory_writeback_request_to_payload_v0(write_back_request)
    write_back_record_payload = memory_writeback_record_to_payload_v0(write_back_record)

    assert comparison.comparison_id == "historical-comparison::alpha"
    assert correction.correction_id == "posterior-correction::alpha"
    assert write_back_request.write_back_id == "memory-writeback::alpha"
    assert write_back_record.write_back_id == "memory-writeback-record::alpha"

    assert correction.subject_id == comparison.subject_id
    assert comparison.comparison_id in correction.correction_basis

    assert write_back_request.subject_id == correction.subject_id
    assert correction.correction_id in write_back_request.source_evidence_refs
    assert comparison.comparison_id in write_back_request.source_evidence_refs

    assert write_back_record.stored_memory_layer == "posterior"
    assert write_back_record.write_back_status == "stored"

    assert comparison_payload["comparison_confidence"] == "medium"
    assert correction_payload["correction_direction"] == "down"
    assert correction_payload["correction_strength"] == "medium"
    assert write_back_request_payload["write_back_mode"] == "structured_posterior_update"
    assert write_back_record_payload["retention_hint"] == "long_term"

    for payload in (
        comparison_payload,
        correction_payload,
        write_back_request_payload,
        write_back_record_payload,
    ):
        for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
            assert field_name not in payload


def test_mmn_object_chain_smoke_v0_light_path() -> None:
    comparison = build_historical_comparison_object_v0(
        comparison_seed="beta",
        subject_id="subject-beta",
        current_pattern_summary="single asset confirmation signal",
        comparison_confidence="low",
    )

    correction = build_posterior_correction_object_v0(
        correction_seed="beta",
        subject_id="subject-beta",
        correction_direction="neutral",
        correction_strength="light",
    )

    write_back_request = build_memory_writeback_request_v0(
        write_back_seed="beta",
        subject_id="subject-beta",
        target_memory_layer=("warm",),
        write_back_mode="preview_only",
    )

    write_back_record = build_memory_writeback_record_v0(
        write_back_seed="beta",
        stored_memory_ref="mem_preview_beta",
        stored_memory_layer="warm",
        stored_memory_kind="preview_memory_note",
        write_back_status="deferred",
        retention_hint="short_term",
    )

    assert comparison.comparison_confidence == "low"
    assert correction.correction_direction == "neutral"
    assert correction.correction_strength == "light"
    assert write_back_request.target_memory_layer == ("warm",)
    assert write_back_request.write_back_mode == "preview_only"
    assert write_back_record.write_back_status == "deferred"
    assert write_back_record.retention_hint == "short_term"
