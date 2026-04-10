from mmn import (
    FORBIDDEN_EXECUTION_FIELDS_V0,
    MemoryPreviewOutputV0,
    MemoryRecordV0,
    MemoryStubProviderV0,
    __version__,
    adapt_memory_preview_for_pant_route_v0,
    build_memory_preview_output_v0,
    build_memory_record_v0,
    build_recall_stub_v0,
    memory_preview_output_to_payload_v0,
    memory_record_to_payload_v0,
)
from mmn import (
    __all__ as mmn_all,
)
from mmn.adapters import __all__ as adapters_all
from mmn.contracts import __all__ as contracts_all
from mmn.providers import __all__ as providers_all
from mmn.recall import __all__ as recall_all


def test_contracts_public_exports_are_stable() -> None:
    assert contracts_all == [
        "ALLOWED_CITATION_HINTS_V0",
        "ALLOWED_MEMORY_STRENGTH_HINTS_V0",
        "ALLOWED_RECORD_KINDS_V0",
        "MEMORY_OUTPUT_MODEL_VERSION_V0",
        "MEMORY_OUTPUT_VERSION_V0",
        "MEMORY_RECORD_VERSION_V0",
        "MemoryPreviewOutputV0",
        "MemoryRecordV0",
        "build_memory_preview_output_v0",
        "build_memory_record_v0",
        "memory_preview_output_to_payload_v0",
        "memory_record_to_payload_v0",
    ]


def test_providers_public_exports_are_stable() -> None:
    assert providers_all == ["MemoryStubProviderV0"]


def test_recall_public_exports_are_stable() -> None:
    assert recall_all == ["build_recall_stub_v0"]


def test_adapters_public_exports_are_stable() -> None:
    assert adapters_all == [
        "FORBIDDEN_EXECUTION_FIELDS_V0",
        "adapt_memory_preview_for_pant_route_v0",
    ]


def test_top_level_public_exports_are_stable() -> None:
    assert mmn_all == [
        "__version__",
        "ALLOWED_CITATION_HINTS_V0",
        "ALLOWED_MEMORY_STRENGTH_HINTS_V0",
        "ALLOWED_RECORD_KINDS_V0",
        "FORBIDDEN_EXECUTION_FIELDS_V0",
        "MEMORY_OUTPUT_MODEL_VERSION_V0",
        "MEMORY_OUTPUT_VERSION_V0",
        "MEMORY_RECORD_VERSION_V0",
        "MemoryPreviewOutputV0",
        "MemoryRecordV0",
        "MemoryStubProviderV0",
        "adapt_memory_preview_for_pant_route_v0",
        "build_memory_preview_output_v0",
        "build_memory_record_v0",
        "build_recall_stub_v0",
        "memory_preview_output_to_payload_v0",
        "memory_record_to_payload_v0",
    ]


def test_top_level_exports_are_importable() -> None:
    assert __version__ == "0.1.0"
    assert MemoryRecordV0.__name__ == "MemoryRecordV0"
    assert MemoryPreviewOutputV0.__name__ == "MemoryPreviewOutputV0"
    assert MemoryStubProviderV0.__name__ == "MemoryStubProviderV0"
    assert callable(build_memory_record_v0)
    assert callable(build_memory_preview_output_v0)
    assert callable(build_recall_stub_v0)
    assert callable(adapt_memory_preview_for_pant_route_v0)
    assert callable(memory_record_to_payload_v0)
    assert callable(memory_preview_output_to_payload_v0)
    assert isinstance(FORBIDDEN_EXECUTION_FIELDS_V0, tuple)
