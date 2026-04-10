import pytest

from mmn.adapters.pant_route_preview_adapter_v0 import adapt_memory_preview_for_pant_route_v0
from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0


def test_pant_route_preview_adapter_rejects_unsupported_version() -> None:
    with pytest.raises(ValueError, match="unsupported memory output version"):
        adapt_memory_preview_for_pant_route_v0({"memory_output_version": "wrong"})


def test_pant_route_preview_adapter_rejects_missing_memory_output_id() -> None:
    with pytest.raises(ValueError, match="missing memory_output_id"):
        adapt_memory_preview_for_pant_route_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_strength_hint": "medium",
                "citation_hint": "limited",
            }
        )


def test_pant_route_preview_adapter_rejects_missing_memory_strength_hint() -> None:
    with pytest.raises(ValueError, match="missing memory_strength_hint"):
        adapt_memory_preview_for_pant_route_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "citation_hint": "limited",
            }
        )


def test_pant_route_preview_adapter_rejects_missing_citation_hint() -> None:
    with pytest.raises(ValueError, match="missing citation_hint"):
        adapt_memory_preview_for_pant_route_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "memory_strength_hint": "medium",
            }
        )


@pytest.mark.parametrize("field_name", ["execution_payload", "dispatch_plan", "db_write"])
def test_pant_route_preview_adapter_blocks_forbidden_execution_fields(
    field_name: str,
) -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False).__dict__.copy()
    output[field_name] = "blocked"

    with pytest.raises(ValueError, match="blocked forbidden execution field"):
        adapt_memory_preview_for_pant_route_v0(output)
