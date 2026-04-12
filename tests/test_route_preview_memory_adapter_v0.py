import pytest

from mmn.adapters.route_preview_memory_adapter_v0 import (
    adapt_memory_preview_for_route_preview_v0,
)
from mmn.contracts.memory_preview_output_v0 import (
    memory_preview_output_to_payload_v0,
)
from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0


def test_route_preview_memory_adapter_shape_is_stable() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False)

    adapted = adapt_memory_preview_for_route_preview_v0(memory_preview_output_to_payload_v0(output))

    assert adapted["memory_semantic_input_version"] == "route_preview_memory_input_v0"
    assert adapted["memory_output_id"] == "memory-preview::alpha"
    assert adapted["memory_strength_hint"] == "medium"
    assert adapted["citation_hint"] == "limited"


def test_route_preview_memory_adapter_is_fail_closed_for_forbidden_field() -> None:
    provider = MemoryStubProviderV0()
    output = memory_preview_output_to_payload_v0(
        provider.generate(output_seed="alpha", richer_memory=False)
    )
    output["worker_target"] = "worker_v0"

    with pytest.raises(ValueError):
        adapt_memory_preview_for_route_preview_v0(output)


def test_route_preview_memory_adapter_rejects_unsupported_version() -> None:
    with pytest.raises(ValueError, match="unsupported memory output version"):
        adapt_memory_preview_for_route_preview_v0({"memory_output_version": "wrong"})


def test_route_preview_memory_adapter_rejects_missing_memory_output_id() -> None:
    with pytest.raises(ValueError, match="missing memory_output_id"):
        adapt_memory_preview_for_route_preview_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_strength_hint": "medium",
                "citation_hint": "limited",
            }
        )


def test_route_preview_memory_adapter_rejects_missing_memory_strength_hint() -> None:
    with pytest.raises(ValueError, match="missing memory_strength_hint"):
        adapt_memory_preview_for_route_preview_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "citation_hint": "limited",
            }
        )


def test_route_preview_memory_adapter_rejects_missing_citation_hint() -> None:
    with pytest.raises(ValueError, match="missing citation_hint"):
        adapt_memory_preview_for_route_preview_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "memory_strength_hint": "medium",
            }
        )


@pytest.mark.parametrize("field_name", ["execution_payload", "dispatch_plan", "db_write"])
def test_route_preview_memory_adapter_blocks_forbidden_execution_fields(
    field_name: str,
) -> None:
    provider = MemoryStubProviderV0()
    output = memory_preview_output_to_payload_v0(
        provider.generate(output_seed="alpha", richer_memory=False)
    )
    output[field_name] = "blocked"

    with pytest.raises(ValueError, match="blocked forbidden execution field"):
        adapt_memory_preview_for_route_preview_v0(output)
