from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_PATH = (
    ROOT
    / "docs/verification/"
    / "MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_PLAN_V0.md"
)
JSON_PATH = (
    ROOT
    / "docs/verification/"
    / "mmn_authority_event_memory_write_request_candidate_preview_plan_v0.json"
)
FIXTURE_PATH = (
    ROOT
    / "tests/fixtures/mmn_authority_event_memory/"
    / "write_request_candidate_preview_plan_v0.json"
)

DOCUMENT_NAME = "MMN_AUTHORITY_EVENT_MEMORY_WRITE_REQUEST_CANDIDATE_PREVIEW_PLAN_V0"
PLAN_KIND = "mmn_authority_event_memory_write_request_candidate_preview_plan_v0"
GOLDEN_SHA = "dbac9b7568c4a3f7b6994d752c1de139ef198309c50534527760d0b941057b90"


def _read_json(path: Path) -> dict[str, Any]:
    return cast(dict[str, Any], json.loads(path.read_text(encoding="utf-8")))


def _candidate_fields(data: dict[str, Any]) -> list[dict[str, Any]]:
    return cast(list[dict[str, Any]], data["candidate_fields"])


def test_mmn_aem_write_request_candidate_preview_plan_doc_exists() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    expected_fragments = [
        "MMN Authority Event Memory Write Request Candidate Preview Plan V0",
        "write request candidate preview plan = preview design plan",
        "write request candidate preview plan != write request schema",
        "write request candidate preview plan != writeback request",
        "write request candidate preview plan != memory record",
        "write request candidate preview plan != memory write authority",
        "Read-only projection is not memory write authority.",
        "Boolean authority fields are derived summaries, not authority sources.",
    ]

    for fragment in expected_fragments:
        assert fragment in text


def test_mmn_aem_write_request_candidate_preview_plan_metadata() -> None:
    data = _read_json(JSON_PATH)

    assert data["document"] == DOCUMENT_NAME
    assert data["plan_kind"] == PLAN_KIND
    assert data["repo"] == "aiant-mmn"
    assert data["fixture"] == str(FIXTURE_PATH.relative_to(ROOT)).replace("\\", "/")
    assert data["docs_test_only"] is True
    assert data["plan_ready"] is True
    assert data["creates_write_request_schema"] is False
    assert data["creates_writeback_request_schema"] is False
    assert data["creates_memory_record_schema"] is False
    assert data["plan_is_memory_write_authority"] is False
    assert data["plan_is_runtime_authorization"] is False
    assert data["golden_fixture_canonical_sha256"] == GOLDEN_SHA


def test_mmn_aem_write_request_candidate_preview_plan_categories() -> None:
    data = _read_json(JSON_PATH)

    assert data["field_categories"] == [
        "identity_and_lineage",
        "read_only_source_refs",
        "grant_candidate_refs",
        "operation_request",
        "payload_boundary",
        "evidence_refs",
        "decision_summary",
        "blocking_and_lifecycle",
        "audit_and_trace",
    ]


def test_mmn_aem_write_request_candidate_preview_plan_fields() -> None:
    data = _read_json(JSON_PATH)
    fields = _candidate_fields(data)

    expected_names = {
        "write_request_candidate_id",
        "write_request_candidate_version",
        "source_read_only_projection_ref",
        "grant_envelope_candidate_ref",
        "grant_envelope_candidate_field_registry_ref",
        "requested_memory_operation",
        "candidate_payload_digest",
        "candidate_payload_summary",
        "required_evidence_refs",
        "receipt_refs",
        "governance_scanner_preview_ref",
        "core_topology_gate_preview_ref",
        "write_candidate_preview_decision",
        "write_candidate_preview_basis",
        "blocking_conditions",
        "deferral_refs",
        "revocation_refs",
        "expiry_policy",
        "preview_output_ref",
        "created_at_utc",
    }

    assert data["field_count"] == len(expected_names)
    assert data["required_field_count"] == len(expected_names)
    assert {str(field["field_name"]) for field in fields} == expected_names


def test_mmn_aem_write_request_candidate_preview_plan_field_shape() -> None:
    data = _read_json(JSON_PATH)
    fields = _candidate_fields(data)
    categories = set(cast(list[str], data["field_categories"]))

    required_keys = {
        "field_name",
        "field_category",
        "value_kind",
        "required_for_preview",
        "default_on_missing",
        "authority_role",
    }

    for field in fields:
        assert set(field) == required_keys
        assert field["field_category"] in categories
        assert field["required_for_preview"] is True
        assert field["default_on_missing"] == "deny_fail_closed"


def test_mmn_aem_write_request_candidate_preview_plan_summary_fields() -> None:
    data = _read_json(JSON_PATH)
    fields = _candidate_fields(data)

    summary_field_names = [
        str(field["field_name"])
        for field in fields
        if field["authority_role"] == "derived_summary_not_authority_source"
    ]

    assert summary_field_names == [
        "candidate_payload_summary",
        "write_candidate_preview_decision",
    ]


def test_mmn_aem_write_request_candidate_preview_plan_phases() -> None:
    data = _read_json(JSON_PATH)
    phases = cast(list[dict[str, Any]], data["phases"])

    assert data["phase_count"] == 5
    assert [str(phase["phase_id"]) for phase in phases] == [
        "phase_0_read_only_projection_input",
        "phase_1_grant_candidate_reference",
        "phase_2_preview_request_assembly",
        "phase_3_governance_and_topology_evidence",
        "phase_4_preview_output_report",
    ]

    decisions = {str(phase["decision"]) for phase in phases}
    assert decisions == {
        "input_only",
        "reference_only",
        "preview_only",
        "report_only",
    }


def test_mmn_aem_write_request_candidate_preview_plan_negative_cases() -> None:
    data = _read_json(JSON_PATH)
    negative_cases = cast(list[dict[str, Any]], data["negative_cases"])

    expected_case_ids = {
        "missing_read_only_projection_denied",
        "missing_grant_envelope_candidate_denied",
        "missing_candidate_registry_denied",
        "missing_governance_preview_denied",
        "missing_core_topology_preview_denied",
        "non_empty_blockers_denied",
        "memory_write_authority_claim_denied",
        "writeback_record_claim_denied",
        "drl_or_trading_claim_denied",
    }

    assert {str(case["case_id"]) for case in negative_cases} == expected_case_ids

    for case in negative_cases:
        assert case["expected_decision"] == "deny_fail_closed"
        assert str(case["required_reason"])


def test_mmn_aem_write_request_candidate_preview_plan_fixture_matches() -> None:
    data = _read_json(JSON_PATH)
    fixture = _read_json(FIXTURE_PATH)

    assert fixture["plan_kind"] == data["plan_kind"]
    assert fixture["golden_fixture_canonical_sha256"] == GOLDEN_SHA
    assert fixture["field_categories"] == data["field_categories"]
    assert fixture["field_count"] == data["field_count"]
    assert fixture["required_field_count"] == data["required_field_count"]
    assert fixture["candidate_fields"] == data["candidate_fields"]
    assert fixture["phases"] == data["phases"]
    assert fixture["negative_cases"] == data["negative_cases"]


def test_mmn_aem_write_request_candidate_preview_plan_principles() -> None:
    data = _read_json(JSON_PATH)
    principles = cast(dict[str, object], data["authority_envelope_principles"])

    assert principles["write_request_candidate_preview_plan_is_not_memory_write_authority"] is True
    assert principles["write_request_candidate_preview_plan_is_not_runtime_authorization"] is True
    assert principles["read_only_projection_is_not_memory_write_authority"] is True
    assert principles["candidate_payload_summary_is_not_authority_source"] is True
    assert (
        principles["boolean_authority_fields_are_derived_summaries_not_authority_sources"] is True
    )
    assert principles["accepted_contract_surface_is_not_downstream_runtime_authorization"] is True
    assert principles["core_topology_reference_is_not_runtime_path_enablement"] is True
    assert principles["default_on_missing_evidence"] == "false_fail_closed"


def test_mmn_aem_write_request_candidate_preview_plan_non_authorizations() -> None:
    data = _read_json(JSON_PATH)
    non_auth = cast(dict[str, bool], data["explicit_non_authorizations"])

    expected = {
        "plan_creates_write_request_schema",
        "plan_creates_writeback_request_schema",
        "plan_creates_memory_record_schema",
        "plan_is_memory_write_authority",
        "plan_is_runtime_authorization",
        "write_request_candidate_preview_is_writeback_request",
        "write_request_candidate_preview_is_memory_record",
        "write_request_candidate_preview_persists_memory",
        "production_adapter_adoption_authorized",
        "downstream_runtime_consumption_authorized",
        "memory_write_authority_granted",
        "memory_record_creation_authorized",
        "memory_writeback_request_authorized",
        "memory_writeback_record_authorized",
        "runtime_topology_path_enabled",
        "scheduler_route_enabled",
        "execution_handoff_enabled",
        "writeback_route_enabled",
        "drl_execution_authority_granted",
        "trading_signal_authorized",
        "future_live_execution_authorized",
        "runtime_canonicalizer_created",
        "production_runtime_canonical_hash_created",
    }

    assert set(non_auth) == expected
    for key in expected:
        assert non_auth[key] is False


def test_mmn_aem_write_request_candidate_preview_plan_followups() -> None:
    data = _read_json(JSON_PATH)

    assert data["recommended_followup_prs"] == [
        ("core: add MMN authority event memory topology gate grant-envelope preview plan v0"),
        ("contracts: draft MMN authority event memory grant decision receipt candidate plan v0"),
        ("mmn: add MMN authority event memory write request candidate preview fixtures v0"),
    ]
