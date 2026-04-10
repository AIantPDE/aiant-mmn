import pytest

from mmn.providers.memory_stub_provider_v0 import MemoryStubProviderV0
from mmn.recall.recall_stub_v0 import build_recall_stub_v0


def test_recall_stub_rejects_unsupported_version() -> None:
    with pytest.raises(ValueError, match="unsupported memory output version"):
        build_recall_stub_v0({"memory_output_version": "wrong"})


def test_recall_stub_rejects_missing_memory_output_id() -> None:
    with pytest.raises(ValueError, match="missing memory_output_id"):
        build_recall_stub_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_strength_hint": "medium",
                "citation_hint": "limited",
            }
        )


def test_recall_stub_rejects_missing_memory_strength_hint() -> None:
    with pytest.raises(ValueError, match="missing memory_strength_hint"):
        build_recall_stub_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "citation_hint": "limited",
            }
        )


def test_recall_stub_rejects_missing_citation_hint() -> None:
    with pytest.raises(ValueError, match="missing citation_hint"):
        build_recall_stub_v0(
            {
                "memory_output_version": "memory_preview_output_v0",
                "memory_output_id": "memory-preview::alpha",
                "memory_strength_hint": "medium",
            }
        )


def test_recall_stub_returns_observe_when_citation_is_limited() -> None:
    provider = MemoryStubProviderV0()
    output = provider.generate(output_seed="alpha", richer_memory=False)

    result = build_recall_stub_v0(output.__dict__)

    assert result["recall_state"] == "memory_recall_observe"
