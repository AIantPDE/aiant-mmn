from __future__ import annotations

import json
from pathlib import Path
from typing import TypeAlias, cast

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

JsonScalar: TypeAlias = str | int | float | bool | None
JsonValue: TypeAlias = JsonScalar | list["JsonValue"] | dict[str, "JsonValue"]

FIXTURES_DIR = Path(__file__).resolve().parent / "fixtures"


def _load_fixture(*parts: str) -> JsonValue:
    path = FIXTURES_DIR.joinpath(*parts)
    data = json.loads(path.read_text(encoding="utf-8"))
    return _canonicalize(data)


def _canonicalize(value: object) -> JsonValue:
    if value is None or isinstance(value, (str, int, float, bool)):
        return value

    if isinstance(value, tuple):
        raw_tuple = cast(tuple[object, ...], value)
        return [_canonicalize(item) for item in raw_tuple]

    if isinstance(value, list):
        raw_list = cast(list[object], value)
        return [_canonicalize(item) for item in raw_list]

    if isinstance(value, dict):
        raw_dict = cast(dict[object, object], value)
        canonical: dict[str, JsonValue] = {}
        for key, item in raw_dict.items():
            canonical[str(key)] = _canonicalize(item)
        return canonical

    msg = f"Unsupported canonicalize value type: {type(value)!r}"
    raise TypeError(msg)


def test_mmn_object_chain_golden_v0_alpha() -> None:
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

    expected_comparison = _load_fixture(
        "mmn_object_chain_v0",
        "historical_comparison_alpha.json",
    )
    expected_correction = _load_fixture(
        "mmn_object_chain_v0",
        "posterior_correction_alpha.json",
    )
    expected_write_back_request = _load_fixture(
        "mmn_object_chain_v0",
        "memory_writeback_request_alpha.json",
    )
    expected_write_back_record = _load_fixture(
        "mmn_object_chain_v0",
        "memory_writeback_record_alpha.json",
    )

    assert _canonicalize(comparison_payload) == expected_comparison
    assert _canonicalize(correction_payload) == expected_correction
    assert _canonicalize(write_back_request_payload) == expected_write_back_request
    assert _canonicalize(write_back_record_payload) == expected_write_back_record

    for payload in (
        comparison_payload,
        correction_payload,
        write_back_request_payload,
        write_back_record_payload,
    ):
        for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
            assert field_name not in payload


def test_mmn_object_chain_golden_v0_light_beta() -> None:
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

    actual = _canonicalize(
        {
            "comparison": historical_comparison_object_to_payload_v0(comparison),
            "correction": posterior_correction_object_to_payload_v0(correction),
            "write_back_request": memory_writeback_request_to_payload_v0(write_back_request),
            "write_back_record": memory_writeback_record_to_payload_v0(write_back_record),
        }
    )
    expected = _load_fixture(
        "mmn_object_chain_v0",
        "mmn_object_chain_light_beta.json",
    )

    assert actual == expected

    assert isinstance(actual, dict)
    for payload in actual.values():
        assert isinstance(payload, dict)
        for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
            assert field_name not in payload
