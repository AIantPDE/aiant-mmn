from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Mapping, Sequence

EXPECTED_SCHEMA = "MMNAuthorityEventMemoryAcceptedV1"
EXPECTED_FAMILY = "MMNAuthorityEventMemoryAcceptedFamilyV1"
EXPECTED_ADAPTER_MODE = "validator_consumer_read_only"
GOLDEN_CANONICAL_SHA256 = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"

REQUIRED_EVIDENCE_KEYS: tuple[str, ...] = (
    "accepted_schema_receipt",
    "accepted_family_receipt",
    "receipt_ledger_entry",
    "field_registry_entry",
    "public_export",
    "downstream_policy",
    "core_topology_enablement",
    "governance_scan_pass",
    "adapter_validation_pass",
    "approval_trace",
)

FORBIDDEN_OPERATION_KEYS: tuple[str, ...] = (
    "memory_write_requested",
    "memory_record_creation_requested",
    "memory_writeback_requested",
    "runtime_consumption_requested",
    "drl_execution_requested",
    "trading_signal_requested",
    "future_live_execution_requested",
)


@dataclass(frozen=True)
class MMNAuthorityEventMemoryReadOnlyValidationReportV0:
    """Read-only validation result; never grants memory-write authority."""

    report_kind: str
    adapter_mode: str
    schema_identity_valid: bool
    family_identity_valid: bool
    canonical_hash_matches: bool
    receipt_refs_present: bool
    downstream_policy_present: bool
    authority_envelope_consistent: bool
    scope_matches: bool
    allowed_to_write_memory: bool
    allowed_to_execute: bool
    fail_closed: bool
    fail_closed_reasons: tuple[str, ...]


def _as_mapping(value: object) -> Mapping[str, Any]:
    if isinstance(value, Mapping):
        return value
    return {}


def _as_sequence(value: object) -> Sequence[object]:
    if isinstance(value, Sequence) and not isinstance(value, str):
        return value
    return ()


def _has_truthy_mapping_values(mapping: Mapping[str, Any], keys: Sequence[str]) -> bool:
    return all(bool(mapping.get(key)) for key in keys)


def validate_mmn_authority_event_memory_read_only(
    payload: Mapping[str, Any],
    *,
    expected_repo: str = "aiant-mmn",
    expected_adapter_mode: str = EXPECTED_ADAPTER_MODE,
) -> MMNAuthorityEventMemoryReadOnlyValidationReportV0:
    """Validate an accepted AEM payload as read-only evidence.

    This stub is intentionally non-executing. It returns a report and never writes
    memory, creates records, emits trading signals, or grants execution authority.
    """

    reasons: list[str] = []

    schema_identity_valid = payload.get("schema") == EXPECTED_SCHEMA
    if not schema_identity_valid:
        reasons.append("schema_identity_mismatch")

    family_identity_valid = payload.get("family") == EXPECTED_FAMILY
    if not family_identity_valid:
        reasons.append("family_identity_mismatch")

    canonical_hash_matches = payload.get("canonical_sha256") == GOLDEN_CANONICAL_SHA256
    if not canonical_hash_matches:
        reasons.append("canonical_hash_mismatch")

    receipts = _as_mapping(payload.get("receipts"))
    receipt_refs_present = bool(receipts.get("accepted_schema_receipt")) and bool(
        receipts.get("accepted_family_receipt")
    )
    if not receipt_refs_present:
        reasons.append("missing_receipt_refs")

    downstream_policy_present = bool(payload.get("downstream_policy"))
    if not downstream_policy_present:
        reasons.append("missing_downstream_policy")

    envelope = _as_mapping(payload.get("authority_envelope"))
    decision_basis = _as_mapping(envelope.get("decision_basis"))
    grant_scope = _as_mapping(envelope.get("grant_scope"))
    required_evidence = tuple(str(item) for item in _as_sequence(envelope.get("required_evidence")))

    required_keys = required_evidence or REQUIRED_EVIDENCE_KEYS
    evidence_complete = _has_truthy_mapping_values(decision_basis, required_keys)
    missing_evidence_empty = not _as_sequence(envelope.get("missing_evidence"))
    blockers_empty = not _as_sequence(envelope.get("blocking_conditions"))
    deferrals_empty = not _as_sequence(envelope.get("deferral_refs"))
    revocations_empty = not _as_sequence(envelope.get("revocation_refs"))

    authority_envelope_consistent = (
        envelope.get("decision") in {"read_only_validated", "granted"}
        and envelope.get("authority_granted") is not True
        and evidence_complete
        and missing_evidence_empty
        and blockers_empty
        and deferrals_empty
        and revocations_empty
        and envelope.get("default_on_missing_evidence") == "false_fail_closed"
    )
    if not authority_envelope_consistent:
        reasons.append("authority_envelope_inconsistent")

    scope_matches = (
        grant_scope.get("repo") == expected_repo
        and grant_scope.get("adapter_mode") == expected_adapter_mode
        and grant_scope.get("schema") == EXPECTED_SCHEMA
        and grant_scope.get("family") == EXPECTED_FAMILY
    )
    if not scope_matches:
        reasons.append("authority_envelope_scope_mismatch")

    for key in FORBIDDEN_OPERATION_KEYS:
        if payload.get(key) is True:
            reasons.append(key)

    fail_closed = bool(reasons)

    return MMNAuthorityEventMemoryReadOnlyValidationReportV0(
        report_kind="mmn_authority_event_memory_read_only_validation_report_v0",
        adapter_mode=expected_adapter_mode,
        schema_identity_valid=schema_identity_valid,
        family_identity_valid=family_identity_valid,
        canonical_hash_matches=canonical_hash_matches,
        receipt_refs_present=receipt_refs_present,
        downstream_policy_present=downstream_policy_present,
        authority_envelope_consistent=authority_envelope_consistent,
        scope_matches=scope_matches,
        allowed_to_write_memory=False,
        allowed_to_execute=False,
        fail_closed=fail_closed,
        fail_closed_reasons=tuple(reasons),
    )
