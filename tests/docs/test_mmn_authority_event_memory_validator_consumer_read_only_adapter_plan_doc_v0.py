from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_NAME = "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_PLAN_V0.md"
JSON_NAME = "mmn_authority_event_memory_validator_consumer_read_only_adapter_plan_v0.json"
FIXTURE_NAME = "validator_consumer_read_only_adapter_plan_v0.json"

DOC_PATH = ROOT / "docs/verification" / DOC_NAME
JSON_PATH = ROOT / "docs/verification" / JSON_NAME
FIXTURE_PATH = ROOT / "tests/fixtures/mmn_authority_event_memory" / FIXTURE_NAME

DOCUMENT_NAME = "MMN_AUTHORITY_EVENT_MEMORY_VALIDATOR_CONSUMER_READ_ONLY_ADAPTER_PLAN_V0"
PLAN_KIND = "mmn_authority_event_memory_validator_consumer_read_only_adapter_plan_v0"
REPORT_KIND = "mmn_authority_event_memory_validator_consumer_read_only_report_v0"
GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"

FOLLOWUP_ADAPTER_STUB = (
    "mmn: add MMN authority event memory validator-consumer read-only adapter fixture and stub v0"
)


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def test_mmn_aem_validator_consumer_read_only_adapter_plan_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        "MMN Authority Event Memory Validator-Consumer Read-Only Adapter Plan V0",
        (
            "MMN validator-consumer "
            "\u53ea\u4ee3\u8868\u53ea\u8bfb\u9a8c\u8bc1"
            "\uff0c\u4e0d\u4ee3\u8868\u8bb0\u5fc6"
            "\u5199\u5165\u6388\u6743"
        ),
        (
            "accepted "
            "\u5408\u540c\u8868\u9762\u6210\u7acb"
            "\uff0c\u4e0d\u7b49\u4e8e\u4e0b\u6e38"
            "\u8fd0\u884c\u65f6\u6d88\u8d39"
            "\u5df2\u7ecf\u6388\u6743"
        ),
        (
            "core "
            "\u62d3\u6251\u5f15\u7528\u6210\u7acb"
            "\uff0c\u4e0d\u7b49\u4e8e\u8fd0\u884c"
            "\u65f6\u8def\u5f84\u5df2\u7ecf\u542f\u7528"
        ),
        (
            "\u5e03\u5c14\u578b authority "
            "\u5b57\u6bb5\u53ea\u80fd\u662f\u6d3e\u751f"
            "\u6458\u8981\uff0c\u4e0d\u80fd\u662f"
            "\u6388\u6743\u6765\u6e90"
        ),
        "\u7981\u6b62\u7684\u64cd\u4f5c",
    ]

    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_validator_consumer_read_only_adapter_plan_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["plan_kind"] == PLAN_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["docs_test_only"] is True
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert data["adapter_mode"] == "validator_consumer_read_only_candidate"
    assert data["mmn_validator_consumer_is_memory_write_authority"] is False
    assert data["accepted_contract_surface_is_downstream_runtime_authorization"] is False
    assert data["core_topology_reference_is_runtime_path_enablement"] is False


def test_mmn_aem_validator_consumer_source_contract_identity() -> None:
    data = _read_json(JSON_PATH)
    source = cast(dict[str, object], data["source_contract"])

    assert source["repo"] == "aiant-contracts"
    assert source["schema"] == "MMNAuthorityEventMemoryAcceptedV1"
    assert source["family"] == "MMNAuthorityEventMemoryAcceptedFamilyV1"
    assert source["surface"] == "accepted_contract_public_export"


def test_mmn_aem_validator_consumer_required_upstream_boundaries() -> None:
    data = _read_json(JSON_PATH)
    boundaries = cast(dict[str, bool], data["required_upstream_boundaries"])

    expected = {
        "contracts_accepted_schema_promotion_execution_v0",
        "contracts_downstream_adoption_boundary_plan_v0",
        "governance_downstream_consumption_scanner_boundary_v0",
        "core_downstream_topology_boundary_v0",
    }
    assert set(boundaries) == expected
    for key in expected:
        assert boundaries[key] is True


def test_mmn_aem_validator_consumer_allowed_operations_are_read_only() -> None:
    data = _read_json(JSON_PATH)

    assert data["allowed_read_only_operations"] == [
        "public_contract_import_check",
        "accepted_schema_identity_check",
        "accepted_family_identity_check",
        "receipt_reference_presence_check",
        "canonical_hash_equality_check",
        "downstream_policy_presence_check",
        "authority_envelope_consistency_check",
        "scope_match_check",
        "fail_closed_reason_collection",
        "read_only_validation_report",
    ]


def test_mmn_aem_validator_consumer_forbidden_operations() -> None:
    data = _read_json(JSON_PATH)

    assert data["forbidden_operations"] == [
        "memory_write",
        "memory_record_creation",
        "memory_writeback_request",
        "memory_writeback_record",
        "runtime_consumption",
        "scheduler_route",
        "execution_handoff",
        "drl_execution",
        "trading_signal_generation",
        "future_live_execution",
        "production_runtime_canonical_hash_creation",
    ]


def test_mmn_aem_validator_consumer_fail_closed_conditions() -> None:
    data = _read_json(JSON_PATH)

    assert data["fail_closed_conditions"] == [
        "missing_public_export",
        "schema_identity_mismatch",
        "family_identity_mismatch",
        "missing_accepted_schema_receipt",
        "missing_accepted_family_receipt",
        "missing_receipt_ledger_entry",
        "missing_field_registry_entry",
        "missing_downstream_policy",
        "missing_core_topology_boundary",
        "missing_governance_scanner_boundary",
        "missing_authority_envelope",
        "authority_envelope_scope_mismatch",
        "non_empty_missing_evidence",
        "non_empty_blocking_conditions",
        "non_empty_deferral_refs",
        "non_empty_revocation_refs",
        "canonical_hash_mismatch",
        "requested_memory_write_or_execution",
    ]


def test_mmn_aem_validator_consumer_authority_booleans_are_not_sources() -> None:
    data = _read_json(JSON_PATH)
    principles = cast(dict[str, object], data["authority_envelope_principles"])

    assert (
        principles["boolean_authority_fields_are_derived_summaries_not_authority_sources"] is True
    )
    assert principles["payload_claim_is_not_authority"] is True
    assert principles["adapter_validation_report_is_not_memory_write_authority"] is True
    assert principles["default_on_missing_evidence"] == "false_fail_closed"
    assert data["boolean_authority_fields_not_sources"] == [
        "mmn_validator_consumer_authorized",
        "memory_write_authority_granted",
        "downstream_runtime_consumption_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    ]


def test_mmn_aem_validator_consumer_read_only_report_shape_is_non_authorizing() -> None:
    data = _read_json(JSON_PATH)
    report = cast(dict[str, object], data["read_only_validation_report_shape"])

    assert report["report_kind"] == REPORT_KIND
    assert report["allowed_to_write_memory"] is False
    assert report["allowed_to_execute"] is False
    assert report["fail_closed_reasons"] == "list[str]"


def test_mmn_aem_validator_consumer_explicit_non_authorizations() -> None:
    data = _read_json(JSON_PATH)
    non_auth = cast(dict[str, bool], data["explicit_non_authorizations"])

    expected = {
        "production_adapter_implemented",
        "runtime_consumption_authorized",
        "mmn_validator_consumer_production_adoption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
        "pant_runtime_execution_authorized",
        "zant_authority_interpretation_expansion_authorized",
        "vant_accepted_semantic_authority_expansion_authorized",
        "runtime_canonicalizer_created",
        "production_runtime_canonical_hash_created",
    }
    assert set(non_auth) == expected
    for key in expected:
        assert non_auth[key] is False


def test_mmn_aem_validator_consumer_fixture_matrix() -> None:
    fixture = _read_json(FIXTURE_PATH)
    cases = cast(list[dict[str, object]], fixture["adapter_case_matrix"])

    assert fixture["plan_kind"] == PLAN_KIND
    assert {str(case["case_id"]) for case in cases} == {
        "valid_read_only_reference",
        "missing_receipt",
        "hash_mismatch",
        "scope_mismatch",
        "memory_write_requested",
    }

    for case in cases:
        assert case["expected_report_only"] is True
        assert case["allowed_to_write_memory"] is False
        assert case["allowed_to_execute"] is False

    fail_closed = {str(case["case_id"]) for case in cases if case["fail_closed"] is True}
    assert fail_closed == {
        "missing_receipt",
        "hash_mismatch",
        "scope_mismatch",
        "memory_write_requested",
    }


def test_mmn_aem_validator_consumer_fixture_authorities_remain_false() -> None:
    fixture = _read_json(FIXTURE_PATH)
    summaries = cast(dict[str, bool], fixture["derived_authority_summaries"])

    expected = {
        "mmn_validator_consumer_production_adoption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
    }
    assert set(summaries) == expected
    for key in expected:
        assert summaries[key] is False


def test_mmn_aem_validator_consumer_followups_are_ordered() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        FOLLOWUP_ADAPTER_STUB,
        "governance: add MMN authority event memory downstream scanner dry-run fixtures v0",
        "core: add MMN authority event memory topology dry-run denied fixtures v0",
    ]
