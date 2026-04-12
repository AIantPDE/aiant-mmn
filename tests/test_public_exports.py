from mmn import (
    FORBIDDEN_EXECUTION_FIELDS_V0,
    HISTORICAL_COMPARISON_VERSION_V0,
    MEMORY_WRITEBACK_REQUEST_VERSION_V0,
    POSTERIOR_CORRECTION_VERSION_V0,
    HistoricalComparisonObjectV0,
    MemoryPreviewOutputV0,
    MemoryRecordV0,
    MemoryStubProviderV0,
    MemoryWriteBackRequestV0,
    PosteriorCorrectionObjectV0,
    __version__,
    adapt_memory_preview_for_route_preview_v0,
    build_historical_comparison_object_v0,
    build_memory_preview_output_v0,
    build_memory_record_v0,
    build_memory_writeback_request_v0,
    build_posterior_correction_object_v0,
    build_recall_stub_v0,
    historical_comparison_object_to_payload_v0,
    memory_preview_output_to_payload_v0,
    memory_record_to_payload_v0,
    memory_writeback_request_to_payload_v0,
    posterior_correction_object_to_payload_v0,
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
        "ALLOWED_COMPARISON_CONFIDENCE_V0",
        "ALLOWED_CORRECTION_DIRECTION_V0",
        "ALLOWED_CORRECTION_STRENGTH_V0",
        "ALLOWED_MEMORY_STRENGTH_HINTS_V0",
        "ALLOWED_RECORD_KINDS_V0",
        "ALLOWED_TARGET_MEMORY_LAYERS_V0",
        "ALLOWED_WRITEBACK_MODES_V0",
        "HISTORICAL_COMPARISON_VERSION_V0",
        "MEMORY_OUTPUT_MODEL_VERSION_V0",
        "MEMORY_OUTPUT_VERSION_V0",
        "MEMORY_RECORD_VERSION_V0",
        "MEMORY_WRITEBACK_REQUEST_VERSION_V0",
        "POSTERIOR_CORRECTION_VERSION_V0",
        "HistoricalComparisonObjectV0",
        "MemoryPreviewOutputV0",
        "MemoryRecordV0",
        "MemoryWriteBackRequestV0",
        "PosteriorCorrectionObjectV0",
        "build_historical_comparison_object_v0",
        "build_memory_preview_output_v0",
        "build_memory_record_v0",
        "build_memory_writeback_request_v0",
        "build_posterior_correction_object_v0",
        "historical_comparison_object_to_payload_v0",
        "memory_preview_output_to_payload_v0",
        "memory_record_to_payload_v0",
        "memory_writeback_request_to_payload_v0",
        "posterior_correction_object_to_payload_v0",
    ]


def test_providers_public_exports_are_stable() -> None:
    assert providers_all == ["MemoryStubProviderV0"]


def test_recall_public_exports_are_stable() -> None:
    assert recall_all == ["build_recall_stub_v0"]


def test_adapters_public_exports_are_stable() -> None:
    assert adapters_all == [
        "FORBIDDEN_EXECUTION_FIELDS_V0",
        "adapt_memory_preview_for_route_preview_v0",
    ]


def test_top_level_public_exports_are_stable() -> None:
    assert mmn_all == [
        "__version__",
        "ALLOWED_CITATION_HINTS_V0",
        "ALLOWED_COMPARISON_CONFIDENCE_V0",
        "ALLOWED_CORRECTION_DIRECTION_V0",
        "ALLOWED_CORRECTION_STRENGTH_V0",
        "ALLOWED_MEMORY_STRENGTH_HINTS_V0",
        "ALLOWED_RECORD_KINDS_V0",
        "ALLOWED_TARGET_MEMORY_LAYERS_V0",
        "ALLOWED_WRITEBACK_MODES_V0",
        "FORBIDDEN_EXECUTION_FIELDS_V0",
        "HISTORICAL_COMPARISON_VERSION_V0",
        "MEMORY_OUTPUT_MODEL_VERSION_V0",
        "MEMORY_OUTPUT_VERSION_V0",
        "MEMORY_RECORD_VERSION_V0",
        "MEMORY_WRITEBACK_REQUEST_VERSION_V0",
        "POSTERIOR_CORRECTION_VERSION_V0",
        "HistoricalComparisonObjectV0",
        "MemoryPreviewOutputV0",
        "MemoryRecordV0",
        "MemoryWriteBackRequestV0",
        "MemoryStubProviderV0",
        "PosteriorCorrectionObjectV0",
        "adapt_memory_preview_for_route_preview_v0",
        "build_historical_comparison_object_v0",
        "build_memory_preview_output_v0",
        "build_memory_record_v0",
        "build_memory_writeback_request_v0",
        "build_posterior_correction_object_v0",
        "build_recall_stub_v0",
        "historical_comparison_object_to_payload_v0",
        "memory_preview_output_to_payload_v0",
        "memory_record_to_payload_v0",
        "memory_writeback_request_to_payload_v0",
        "posterior_correction_object_to_payload_v0",
    ]


def test_top_level_exports_are_importable() -> None:
    assert __version__ == "0.1.0"
    assert HistoricalComparisonObjectV0.__name__ == "HistoricalComparisonObjectV0"
    assert PosteriorCorrectionObjectV0.__name__ == "PosteriorCorrectionObjectV0"
    assert MemoryWriteBackRequestV0.__name__ == "MemoryWriteBackRequestV0"
    assert MemoryRecordV0.__name__ == "MemoryRecordV0"
    assert MemoryPreviewOutputV0.__name__ == "MemoryPreviewOutputV0"
    assert MemoryStubProviderV0.__name__ == "MemoryStubProviderV0"
    assert HISTORICAL_COMPARISON_VERSION_V0 == "historical_comparison_object_v0"
    assert POSTERIOR_CORRECTION_VERSION_V0 == "posterior_correction_object_v0"
    assert MEMORY_WRITEBACK_REQUEST_VERSION_V0 == "memory_writeback_request_v0"
    assert callable(build_historical_comparison_object_v0)
    assert callable(build_posterior_correction_object_v0)
    assert callable(build_memory_writeback_request_v0)
    assert callable(build_memory_record_v0)
    assert callable(build_memory_preview_output_v0)
    assert callable(build_recall_stub_v0)
    assert callable(adapt_memory_preview_for_route_preview_v0)
    assert callable(historical_comparison_object_to_payload_v0)
    assert callable(posterior_correction_object_to_payload_v0)
    assert callable(memory_writeback_request_to_payload_v0)
    assert callable(memory_record_to_payload_v0)
    assert callable(memory_preview_output_to_payload_v0)
    assert isinstance(FORBIDDEN_EXECUTION_FIELDS_V0, tuple)
