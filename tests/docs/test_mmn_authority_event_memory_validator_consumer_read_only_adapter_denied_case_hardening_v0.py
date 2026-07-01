from __future__ import annotations

import importlib.util
import json
import sys
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

STUB_PATH = (
    ROOT
    / "src/aiant_mmn/"
    / "mmn_authority_event_memory_validator_consumer_read_only_adapter_v0.py"
)
DOC_PATH = (
    ROOT
    / "docs/verification/"
    / (
        "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_"
        "DENIED_CASE_HARDENING_V0.md"
    )
)
JSON_PATH = (
    ROOT
    / "docs/verification/"
    / (
        "mmn_authority_event_memory_validator_consumer_read_only_adapter_"
        "denied_case_hardening_v0.json"
    )
)
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/mmn_authority_event_memory/"
    / "validator_consumer_read_only_adapter_denied_case_hardening_v0.json"
)

DOCUMENT_NAME = (
    "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_DENIED_CASE_HARDENING_V0"
)
HARDENING_KIND = (
    "mmn_authority_event_memory_validator_consumer_read_only_adapter_denied_case_hardening_v0"
)
REPORT_KIND = "mmn_authority_event_memory_read_only_validation_report_v0"
GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"


class StubModuleProtocol:
    validate_mmn_authority_event_memory_read_only: Any
    EXPECTED_FAIL_CLOSED_REASONS: tuple[str, ...]


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _load_stub() -> StubModuleProtocol:
    spec = importlib.util.spec_from_file_location("mmn_aem_read_only_stub_v0", STUB_PATH)
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return cast(StubModuleProtocol, module)


def test_mmn_aem_read_only_denied_case_hardening_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        (
            "MMN Authority Event Memory Validator-Consumer Read-Only Adapter "
            "Denied Case Hardening V0"
        ),
        "MMN validator-consumer read-only validation report is not memory write authority.",
        "Accepted contract surface is not downstream runtime authorization.",
        "Boolean authority fields are derived summaries, not authority sources.",
        "missing_public_export",
        "non_empty_revocation_refs",
        "requested_memory_write_or_execution",
    ]

    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_read_only_denied_case_hardening_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["hardening_kind"] == HARDENING_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["source_stub"] == str(STUB_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["fixture"] == str(FIXTURE_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["production_adapter_implemented"] is False
    assert data["validator_consumer_is_read_only"] is True
    assert data["read_only_validation_report_is_memory_write_authority"] is False
    assert data["allowed_to_write_memory_default"] is False
    assert data["allowed_to_execute_default"] is False
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA


def test_mmn_aem_read_only_denied_case_hardening_reasons_exported() -> None:
    module = _load_stub()
    data = _read_json(JSON_PATH)

    expected = tuple(cast(list[str], data["expected_hardened_fail_closed_reasons"]))

    assert module.EXPECTED_FAIL_CLOSED_REASONS == expected
    assert "missing_public_export" in expected
    assert "missing_authority_envelope" in expected
    assert "requested_memory_write_or_execution" in expected


def test_mmn_aem_read_only_denied_case_hardening_valid_case_reports_only() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])
    case = cases[0]

    report = module.validate_mmn_authority_event_memory_read_only(case["payload"])

    assert report.report_kind == REPORT_KIND
    assert report.schema_identity_valid is True
    assert report.family_identity_valid is True
    assert report.canonical_hash_matches is True
    assert report.receipt_refs_present is True
    assert report.receipt_ledger_entry_present is True
    assert report.field_registry_entry_present is True
    assert report.public_export_present is True
    assert report.downstream_policy_present is True
    assert report.core_topology_boundary_present is True
    assert report.governance_scanner_boundary_present is True
    assert report.required_evidence_complete is True
    assert report.authority_envelope_consistent is True
    assert report.scope_matches is True
    assert report.allowed_to_write_memory is False
    assert report.allowed_to_execute is False
    assert report.fail_closed is False
    assert report.fail_closed_reasons == ()


def test_mmn_aem_read_only_denied_case_hardening_cases_fail_closed() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    assert fixture["hardening_case_count"] == len(cases)
    assert len(cases) == 14

    for case in cases[1:]:
        expected = cast(dict[str, Any], case["expected_report"])
        report = module.validate_mmn_authority_event_memory_read_only(case["payload"])

        assert report.allowed_to_write_memory is False
        assert report.allowed_to_execute is False
        assert report.fail_closed is expected["fail_closed"]
        assert report.fail_closed is True

        for reason in cast(list[str], expected["fail_closed_reasons"]):
            assert reason in report.fail_closed_reasons


def test_mmn_aem_read_only_denied_case_hardening_missing_evidence_cases() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = {
        str(case["case_id"]): cast(dict[str, Any], case)
        for case in cast(list[dict[str, Any]], fixture["cases"])
    }

    expected_pairs = {
        "missing_public_export_denied": "missing_public_export",
        "missing_receipt_ledger_entry_denied": "missing_receipt_ledger_entry",
        "missing_field_registry_entry_denied": "missing_field_registry_entry",
        "missing_core_topology_boundary_denied": "missing_core_topology_boundary",
        ("missing_governance_scanner_boundary_denied"): "missing_governance_scanner_boundary",
    }

    for case_id, reason in expected_pairs.items():
        report = module.validate_mmn_authority_event_memory_read_only(cases[case_id]["payload"])
        assert reason in report.fail_closed_reasons
        assert "authority_envelope_inconsistent" in report.fail_closed_reasons


def test_mmn_aem_read_only_denied_case_hardening_non_empty_lists() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = {
        str(case["case_id"]): cast(dict[str, Any], case)
        for case in cast(list[dict[str, Any]], fixture["cases"])
    }

    expected_pairs = {
        "non_empty_missing_evidence_denied": "non_empty_missing_evidence",
        "non_empty_blocking_conditions_denied": "non_empty_blocking_conditions",
        "non_empty_deferral_refs_denied": "non_empty_deferral_refs",
        "non_empty_revocation_refs_denied": "non_empty_revocation_refs",
    }

    for case_id, reason in expected_pairs.items():
        report = module.validate_mmn_authority_event_memory_read_only(cases[case_id]["payload"])
        assert reason in report.fail_closed_reasons
        assert "authority_envelope_inconsistent" in report.fail_closed_reasons


def test_mmn_aem_read_only_denied_case_hardening_authority_claims() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = {
        str(case["case_id"]): cast(dict[str, Any], case)
        for case in cast(list[dict[str, Any]], fixture["cases"])
    }

    expected_pairs = {
        "authority_summary_true_denied": "memory_write_authority_granted",
        "runtime_consumption_requested_denied": "runtime_consumption_requested",
        "drl_execution_requested_denied": "drl_execution_requested",
    }

    for case_id, reason in expected_pairs.items():
        report = module.validate_mmn_authority_event_memory_read_only(cases[case_id]["payload"])
        assert "requested_memory_write_or_execution" in report.fail_closed_reasons
        assert reason in report.fail_closed_reasons
        assert report.allowed_to_write_memory is False
        assert report.allowed_to_execute is False


def test_mmn_aem_read_only_denied_case_hardening_non_authorizations() -> None:
    data = _read_json(JSON_PATH)
    non_auth = cast(dict[str, bool], data["explicit_non_authorizations"])

    expected = {
        "production_adapter_adoption_authorized",
        "runtime_consumption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
        "runtime_canonicalizer_created",
        "production_runtime_canonical_hash_created",
    }
    assert set(non_auth) == expected
    for key in expected:
        assert non_auth[key] is False


def test_mmn_aem_read_only_denied_case_hardening_followups_are_ordered() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        "core: add MMN authority event memory topology gate skeleton v0",
        "governance: wire MMN authority event memory scanner check-path preview v0",
        "mmn: add MMN authority event memory read-only adapter report projection v0",
    ]
