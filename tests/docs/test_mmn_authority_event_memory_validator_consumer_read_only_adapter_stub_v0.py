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
    / "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_STUB_V0.md"
)
JSON_PATH = (
    ROOT
    / "docs/verification/"
    / "mmn_authority_event_memory_validator_consumer_read_only_adapter_stub_v0.json"
)
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/mmn_authority_event_memory/"
    / "validator_consumer_read_only_adapter_stub_v0.json"
)

GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"
DOCUMENT_NAME = "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_STUB_V0"
STUB_KIND = "mmn_authority_event_memory_validator_consumer_read_only_adapter_stub_v0"
REPORT_KIND = "mmn_authority_event_memory_read_only_validation_report_v0"


class StubModuleProtocol:
    validate_mmn_authority_event_memory_read_only: Any


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _load_stub() -> Any:
    spec = importlib.util.spec_from_file_location(
        "mmn_aem_read_only_stub_v0",
        STUB_PATH,
    )
    assert spec is not None
    assert spec.loader is not None

    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


def test_mmn_aem_read_only_adapter_stub_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        "MMN Authority Event Memory Validator-Consumer Read-Only Adapter Stub V0",
        (
            "MMN "
            "\u53ea\u8bfb\u9a8c\u8bc1\u62a5\u544a"
            "\u4e0d\u7b49\u4e8e\u8bb0\u5fc6\u5199\u5165\u6388\u6743"
        ),
        ("\u5e03\u5c14\u578b authority \u5b57\u6bb5\u53ea\u80fd\u662f\u6d3e\u751f\u6458\u8981"),
        "memory_write_requested",
        "production runtime canonical hash",
    ]
    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_read_only_adapter_stub_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["stub_kind"] == STUB_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["docs_test_only"] is True
    assert data["source_stub"] == str(STUB_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["fixture"] == str(FIXTURE_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert data["read_only_validation_report_is_memory_write_authority"] is False
    assert data["production_adapter_implemented"] is False
    assert data["allowed_to_write_memory_default"] is False
    assert data["allowed_to_execute_default"] is False


def test_mmn_aem_read_only_adapter_stub_exports() -> None:
    data = _read_json(JSON_PATH)

    assert data["stub_exports"] == [
        "MMNAuthorityEventMemoryReadOnlyValidationReportV0",
        "validate_mmn_authority_event_memory_read_only",
    ]


def test_mmn_aem_read_only_adapter_stub_fail_closed_reasons_are_registered() -> None:
    data = _read_json(JSON_PATH)

    assert data["expected_fail_closed_reasons"] == [
        "schema_identity_mismatch",
        "family_identity_mismatch",
        "canonical_hash_mismatch",
        "missing_receipt_refs",
        "missing_downstream_policy",
        "authority_envelope_inconsistent",
        "authority_envelope_scope_mismatch",
        "memory_write_requested",
        "memory_record_creation_requested",
        "memory_writeback_requested",
        "runtime_consumption_requested",
        "drl_execution_requested",
        "trading_signal_requested",
        "future_live_execution_requested",
    ]


def test_mmn_aem_read_only_adapter_fixture_cases() -> None:
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, object]], fixture["cases"])

    assert fixture["fixture_name"] == STUB_KIND
    assert fixture["adapter_mode"] == "validator_consumer_read_only"
    assert fixture["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert {str(case["case_id"]) for case in cases} == {
        "valid_read_only_payload",
        "missing_receipt_denied",
        "canonical_hash_mismatch_denied",
        "scope_mismatch_denied",
        "memory_write_requested_denied",
    }


def test_mmn_aem_read_only_adapter_valid_case_reports_only() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    case = cast(dict[str, Any], fixture["cases"][0])

    report = module.validate_mmn_authority_event_memory_read_only(case["payload"])

    assert report.report_kind == REPORT_KIND
    assert report.schema_identity_valid is True
    assert report.family_identity_valid is True
    assert report.canonical_hash_matches is True
    assert report.receipt_refs_present is True
    assert report.downstream_policy_present is True
    assert report.authority_envelope_consistent is True
    assert report.scope_matches is True
    assert report.allowed_to_write_memory is False
    assert report.allowed_to_execute is False
    assert report.fail_closed is False
    assert report.fail_closed_reasons == ()


def test_mmn_aem_read_only_adapter_denied_cases_fail_closed() -> None:
    module = _load_stub()
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, Any]], fixture["cases"])

    for case in cases[1:]:
        expected = cast(dict[str, Any], case["expected_report"])
        report = module.validate_mmn_authority_event_memory_read_only(case["payload"])

        assert report.allowed_to_write_memory is False
        assert report.allowed_to_execute is False
        assert report.fail_closed is expected["fail_closed"]
        for reason in cast(list[str], expected["fail_closed_reasons"]):
            assert reason in report.fail_closed_reasons


def test_mmn_aem_read_only_adapter_fixture_authorities_remain_false() -> None:
    fixture = _read_json(FIXTURE_PATH)
    non_auth = cast(dict[str, bool], fixture["explicit_non_authorizations"])

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


def test_mmn_aem_read_only_adapter_followups_are_ordered() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        "governance: add MMN authority event memory downstream scanner dry-run fixtures v0",
        "core: add MMN authority event memory topology dry-run denied fixtures v0",
        (
            "mmn: add MMN authority event memory validator-consumer read-only "
            "adapter denied cases v0"
        ),
    ]
