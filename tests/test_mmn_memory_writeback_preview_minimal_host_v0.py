from __future__ import annotations

import pytest

from mmn.contracts.memory_writeback_preview_v0 import (
    FORBIDDEN_EXECUTION_FIELDS_V0,
    build_memory_writeback_preview_v0,
    memory_writeback_preview_to_payload_v0,
)


def test_memory_writeback_preview_minimal_host_is_reference_only() -> None:
    preview = build_memory_writeback_preview_v0(
        preview_seed="alpha",
        source_memory_output_id="memory-preview::alpha",
        reason_codes=("MEMORY_PREVIEW", "MEMORY_PREVIEW"),
        evidence_refs=("memory-preview::alpha", "trace::alpha"),
    )

    assert preview.preview_version == "memory_writeback_preview_v0"
    assert preview.preview_id == "memory-writeback-preview::alpha"
    assert preview.source_memory_output_id == "memory-preview::alpha"
    assert preview.preview_state == "reference_only_preview"
    assert preview.reason_codes == ("MEMORY_PREVIEW",)
    assert preview.evidence_refs == ("memory-preview::alpha", "trace::alpha")
    assert preview.memory_write_authorized is False
    assert preview.persistent_memory_mutation_authorized is False
    assert preview.runtime_authority_granted is False


def test_memory_writeback_preview_payload_retains_closed_authority() -> None:
    preview = build_memory_writeback_preview_v0(
        preview_seed="beta",
        source_memory_output_id="memory-preview::beta",
    )
    payload = memory_writeback_preview_to_payload_v0(preview)

    assert payload["preview_state"] == "reference_only_preview"
    assert payload["memory_write_authorized"] is False
    assert payload["persistent_memory_mutation_authorized"] is False
    assert payload["runtime_authority_granted"] is False
    assert payload["trace"] == {
        "source_stage": "memory_writeback_preview_v0",
        "preview_id": "memory-writeback-preview::beta",
        "source_memory_output_id": "memory-preview::beta",
        "preview_state": "reference_only_preview",
        "reason_codes": (),
        "evidence_refs": (),
        "memory_write_authorized": False,
        "persistent_memory_mutation_authorized": False,
        "runtime_authority_granted": False,
    }


@pytest.mark.parametrize("field", sorted(FORBIDDEN_EXECUTION_FIELDS_V0))
def test_memory_writeback_preview_rejects_execution_like_fields(field: str) -> None:
    with pytest.raises(ValueError, match="forbidden execution-like fields"):
        build_memory_writeback_preview_v0(
            preview_seed="gamma",
            source_memory_output_id="memory-preview::gamma",
            material={field: True},
        )


def test_memory_writeback_preview_rejects_invalid_normalization_shape() -> None:
    with pytest.raises(ValueError, match="value must be a string, list, tuple, or None"):
        build_memory_writeback_preview_v0(
            preview_seed="delta",
            source_memory_output_id="memory-preview::delta",
            evidence_refs={"trace::delta"},  # type: ignore[arg-type]
        )
