from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0


def test_memory_stub_provider_output_is_stable() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False)

    assert output.memory_output_id == "memory-preview::alpha"
    assert output.memory_strength_hint == "medium"
    assert output.citation_hint == "limited"
    assert len(output.records) == 2
