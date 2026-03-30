import pytest

from mmn.adapters.pant_route_preview_adapter_v0 import adapt_memory_preview_for_pant_route_v0
from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0


def test_pant_route_preview_adapter_shape_is_stable() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False)

    adapted = adapt_memory_preview_for_pant_route_v0(output.__dict__)

    assert adapted["memory_semantic_input_version"] == "pant_route_memory_input_v0"
    assert adapted["memory_output_id"] == "memory-preview::alpha"
    assert adapted["memory_strength_hint"] == "medium"
    assert adapted["citation_hint"] == "limited"


def test_pant_route_preview_adapter_is_fail_closed_for_forbidden_field() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False).__dict__.copy()
    output["worker_target"] = "worker_v0"

    with pytest.raises(ValueError):
        adapt_memory_preview_for_pant_route_v0(output)
