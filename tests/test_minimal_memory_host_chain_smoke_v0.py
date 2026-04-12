from mmn.adapters.route_preview_memory_adapter_v0 import (
    FORBIDDEN_EXECUTION_FIELDS_V0,
    adapt_memory_preview_for_route_preview_v0,
)
from mmn.contracts.memory_preview_output_v0 import (
    memory_preview_output_to_payload_v0,
)
from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0
from mmn.recall.recall_stub_v0 import build_recall_stub_v0


def test_minimal_memory_host_chain_smoke_richer_path() -> None:
    provider = MemoryStubProviderV0()

    output = provider.generate(output_seed="alpha", richer_memory=True)
    output_payload = memory_preview_output_to_payload_v0(output)
    recall = build_recall_stub_v0(output_payload)
    adapted = adapt_memory_preview_for_route_preview_v0(output_payload)

    assert output.memory_output_version == "memory_preview_output_v0"
    assert output.memory_output_id == "memory-preview::alpha"
    assert output.memory_strength_hint == "strong"
    assert output.citation_hint == "available"
    assert output.reason_codes == ("MEMORY_STUB", "RICHER_MEMORY")
    assert len(output.records) == 2

    assert recall["recall_version"] == "recall_stub_v0"
    assert recall["recall_id"] == "memory-recall::memory-preview::alpha"
    assert recall["memory_output_id"] == output.memory_output_id
    assert recall["recall_state"] == "memory_recall_preferred"
    assert recall["reason_codes"] == output.reason_codes

    assert adapted["memory_semantic_input_version"] == "route_preview_memory_input_v0"
    assert adapted["memory_semantic_input_id"] == "route-preview-memory::memory-preview::alpha"
    assert (
        adapted["memory_output_id"] == output.memory_id
        if hasattr(output, "memory_id")
        else output.memory_output_id
    )
    assert adapted["memory_strength_hint"] == output.memory_strength_hint
    assert adapted["citation_hint"] == output.citation_hint
    assert adapted["reason_codes"] == output.reason_codes

    for field_name in FORBIDDEN_EXECUTION_FIELDS_V0:
        assert field_name not in adapted


def test_minimal_memory_host_chain_smoke_default_path() -> None:
    provider = MemoryStubProviderV0()

    output = provider.generate(output_seed="beta", richer_memory=False)
    output_payload = memory_preview_output_to_payload_v0(output)
    recall = build_recall_stub_v0(output_payload)
    adapted = adapt_memory_preview_for_route_preview_v0(output_payload)

    assert output.memory_output_id == "memory-preview::beta"
    assert output.memory_strength_hint == "medium"
    assert output.citation_hint == "limited"
    assert output.reason_codes == ("MEMORY_STUB",)

    assert recall["memory_output_id"] == output.memory_output_id
    assert recall["recall_state"] == "memory_recall_observe"

    assert adapted["memory_output_id"] == output.memory_output_id
    assert adapted["memory_strength_hint"] == "medium"
    assert adapted["citation_hint"] == "limited"
