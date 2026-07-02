from __future__ import annotations

from collections.abc import Mapping, Sequence
from dataclasses import dataclass

EXPECTED_SOURCE_REPORT_KIND = "mmn_authority_event_memory_read_only_validation_report_v0"
EXPECTED_PROJECTION_KIND = "mmn_authority_event_memory_read_only_adapter_report_projection_v0"
EXPECTED_ADAPTER_MODE = "validator_consumer_read_only"

PROJECT_READ_ONLY_REPORT_DECISION = "project_read_only_report"
PROJECT_FAIL_CLOSED_REPORT_DECISION = "project_fail_closed_report"
NO_RUNTIME_AUTHORIZATION_ACTION = "no_runtime_authorization"
PRESERVE_FAIL_CLOSED_ACTION = "preserve_fail_closed"


@dataclass(frozen=True)
class MMNAuthorityEventMemoryReadOnlyAdapterReportProjectionV0:
    """Projection from read-only adapter report to a non-authorizing summary."""

    projection_kind: str
    source_report_kind: str
    adapter_mode: str
    projection_decision: str
    projection_action: str
    projected_status: str
    source_fail_closed: bool
    fail_closed: bool
    fail_closed_reasons: tuple[str, ...]
    report_projection_is_memory_write_authority: bool = False
    report_projection_is_runtime_authorization: bool = False
    allowed_to_write_memory: bool = False
    allowed_to_execute: bool = False
    downstream_runtime_consumption_authorized: bool = False
    mmn_validator_consumer_production_adoption_authorized: bool = False
    memory_write_authority_granted: bool = False
    drl_execution_authority_granted: bool = False
    trading_signal_authorized: bool = False
    future_live_execution_authorized: bool = False


def _get(source: object, key: str, default: object = None) -> object:
    if isinstance(source, Mapping):
        return source.get(key, default)
    return getattr(source, key, default)


def _text(value: object, default: str = "") -> str:
    if value is None:
        return default
    return str(value)


def _bool(value: object) -> bool:
    return value is True


def _as_reason_tuple(value: object) -> tuple[str, ...]:
    if isinstance(value, Sequence) and not isinstance(value, str):
        return tuple(str(item) for item in value)
    return ()


def project_mmn_authority_event_memory_read_only_adapter_report_v0(
    report: object,
) -> MMNAuthorityEventMemoryReadOnlyAdapterReportProjectionV0:
    """Project a read-only adapter validation report without granting authority."""

    source_report_kind = _text(_get(report, "report_kind"), "unknown_report_kind")
    adapter_mode = _text(_get(report, "adapter_mode"), "unknown_adapter_mode")
    source_fail_closed = _bool(_get(report, "fail_closed"))
    source_reasons = list(_as_reason_tuple(_get(report, "fail_closed_reasons")))

    projection_reasons: list[str] = list(source_reasons)

    if source_report_kind != EXPECTED_SOURCE_REPORT_KIND:
        projection_reasons.append("unexpected_source_report_kind")

    if adapter_mode != EXPECTED_ADAPTER_MODE:
        projection_reasons.append("unexpected_adapter_mode")

    if _bool(_get(report, "allowed_to_write_memory")) or _bool(_get(report, "allowed_to_execute")):
        projection_reasons.append("source_report_requested_write_or_execution")

    fail_closed = bool(source_fail_closed or projection_reasons)

    if fail_closed:
        return MMNAuthorityEventMemoryReadOnlyAdapterReportProjectionV0(
            projection_kind=EXPECTED_PROJECTION_KIND,
            source_report_kind=source_report_kind,
            adapter_mode=adapter_mode,
            projection_decision=PROJECT_FAIL_CLOSED_REPORT_DECISION,
            projection_action=PRESERVE_FAIL_CLOSED_ACTION,
            projected_status="fail_closed_report_only",
            source_fail_closed=source_fail_closed,
            fail_closed=True,
            fail_closed_reasons=tuple(dict.fromkeys(projection_reasons)),
        )

    return MMNAuthorityEventMemoryReadOnlyAdapterReportProjectionV0(
        projection_kind=EXPECTED_PROJECTION_KIND,
        source_report_kind=source_report_kind,
        adapter_mode=adapter_mode,
        projection_decision=PROJECT_READ_ONLY_REPORT_DECISION,
        projection_action=NO_RUNTIME_AUTHORIZATION_ACTION,
        projected_status="read_only_validated_report_only",
        source_fail_closed=False,
        fail_closed=False,
        fail_closed_reasons=(),
    )
