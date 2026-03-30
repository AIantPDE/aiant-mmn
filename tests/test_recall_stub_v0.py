from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0
from mmn.recall.recall_stub_v0 import build_recall_stub_v0


def test_recall_stub_is_deterministic() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=True)

    result = build_recall_stub_v0(output.__dict__)

    assert result["recall_version"] == "recall_stub_v0"
    assert result["memory_output_id"] == "memory-preview::alpha"
    assert result["recall_state"] == "memory_recall_preferred"
