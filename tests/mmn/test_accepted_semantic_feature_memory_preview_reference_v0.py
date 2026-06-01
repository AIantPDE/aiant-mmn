from __future__ import annotations

import json
from pathlib import Path
from typing import Any, cast

ROOT = Path(__file__).resolve().parents[2]

DOC_PATH = ROOT / "docs" / "mmn" / ("ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_V0.md")

REFERENCE_PATH = (
    ROOT / "mmn" / "references" / ("accepted_semantic_feature_memory_preview_reference_v0.json")
)


JsonObject = dict[str, Any]


def load_reference() -> JsonObject:
    return cast(JsonObject, json.loads(REFERENCE_PATH.read_text(encoding="utf-8")))


def test_mmn_vb_next_files_exist() -> None:
    assert DOC_PATH.exists()
    assert REFERENCE_PATH.exists()


def test_mmn_vb_next_doc_declares_scope() -> None:
    text = DOC_PATH.read_text(encoding="utf-8")

    required_fragments = [
        "Mmn-VB-next",
        "BiasAuditedSemanticFeatureViewContractV0",
        "accepted_semantic_feature_memory_preview_reference_created=True",
        "mmn_adoption_boundary=memory_preview_reference_without_write",
        "next_memory_preview_mapping_review_required=True",
        "memory_write_authorized=False",
        "persistent_memory_mutation_authorized=False",
        "execution_payload_enabled=False",
        "MMN_VB_NEXT_ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_READY",
    ]

    for fragment in required_fragments:
        assert fragment in text


def test_mmn_vb_next_reference_shape() -> None:
    reference = load_reference()

    assert reference["reference_id"] == "accepted_semantic_feature_memory_preview_reference_v0"
    assert reference["reference_version"] == "accepted_semantic_feature_memory_preview_reference_v0"
    assert reference["stage"] == "Mmn-VB-next"
    assert reference["repo"] == "aiant-mmn"
    assert (
        reference["reference_status"] == "ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_READY"
    )
    assert reference["target_contract"] == "BiasAuditedSemanticFeatureViewContractV0"
    assert reference["target_contract_family"] == "bias_audited_semantic_feature_view"


def test_mmn_vb_next_source_refs_are_locked() -> None:
    reference = load_reference()

    assert reference["source_contract_stage"] == "C-VB-14Q"
    assert reference["source_contract_status"] == "accepted_contract_family_registered"
    assert reference["source_governance_stage"] == "G-VB-8"
    assert reference["source_governance_decision_status"] == "approved_for_preview_only"


def test_mmn_vb_next_memory_boundary_is_preview_only() -> None:
    reference = load_reference()

    assert reference["mmn_adoption_boundary"] == "memory_preview_reference_without_write"
    assert reference["accepted_semantic_feature_memory_preview_reference_created"] is True
    assert reference["stable_cross_repo_contract_surface"] is True
    assert reference["mmn_reference_allowed"] is True
    assert reference["mmn_memory_preview_reference_allowed"] is True
    assert reference["mmn_preview_mapping_planned"] is True
    assert reference["mmn_memory_preview_adapter_created"] is False
    assert reference["mmn_runtime_memory_write_enabled"] is False
    assert reference["mmn_persistent_memory_mutation_authorized"] is False
    assert reference["mmn_execution_payload_enabled"] is False


def test_mmn_vb_next_reference_dimensions_are_locked() -> None:
    reference = load_reference()

    assert reference["memory_preview_reference_dimensions"] == [
        "contract_identity",
        "schema_surface_reference",
        "memory_preview_boundary",
        "preview_mapping_boundary",
        "memory_write_boundary",
        "persistent_mutation_boundary",
        "execution_payload_boundary",
        "rollback_or_deferral_path",
    ]


def test_mmn_vb_next_required_reference_fields_are_locked() -> None:
    reference = load_reference()

    assert reference["required_reference_fields"] == [
        "reference_id",
        "reference_version",
        "target_contract",
        "target_contract_family",
        "source_contract_stage",
        "source_governance_stage",
        "mmn_adoption_boundary",
        "memory_preview_reference_dimensions",
        "authority_flags",
        "next_memory_preview_mapping_review_required",
        "reason_codes",
    ]


def test_mmn_vb_next_memory_preview_mapping_review_is_required() -> None:
    reference = load_reference()

    assert reference["next_memory_preview_mapping_review_required"] is True
    assert reference["memory_preview_mapping_review_required_before_write"] is True
    assert reference["memory_preview_mapping_review_required_before_persistent_mutation"] is True
    assert reference["memory_preview_mapping_review_required_before_execution_payload"] is True


def test_mmn_vb_next_authority_flags_are_false() -> None:
    reference = load_reference()
    flags = reference["authority_flags"]

    assert flags["preview_only"] is True

    false_flags = [
        "runtime_authority_granted",
        "memory_write_authorized",
        "persistent_memory_mutation_authorized",
        "formal_execution_payload_enabled",
        "runtime_execution_enabled",
        "provider_backend_call_enabled",
        "model_call_enabled",
        "worker_coupling_enabled",
        "scheduler_apply_enabled",
        "execution_payload_enabled",
    ]

    for flag in false_flags:
        assert flags[flag] is False


def test_mmn_vb_next_allowed_and_blocked_work_are_locked() -> None:
    reference = load_reference()

    assert reference["allowed_next_work"] == [
        "docs/test accepted semantic feature memory preview mapping reference v0",
        "docs/test mmn accepted semantic feature preview fixture v0",
        "docs/test mmn memory-write denial fixture v0",
    ]
    assert reference["blocked_until_review"] == [
        "memory_write",
        "persistent_memory_mutation",
        "formal_execution_payload",
        "runtime_execution",
        "worker_coupling",
    ]


def test_mmn_vb_next_next_stage_is_locked() -> None:
    reference = load_reference()

    assert reference["recommended_next_stage"] == "Zant-VB-next"
    assert (
        reference["recommended_next_stage_title"]
        == "docs/test: add accepted semantic feature explanation reference v0"
    )


def test_mmn_vb_next_smoke_prints_status_for_s_run() -> None:
    reference = load_reference()
    flags = reference["authority_flags"]

    print("MMN_VB_NEXT_ACCEPTED_SEMANTIC_FEATURE_MEMORY_PREVIEW_REFERENCE_READY")
    print(f"target_contract={reference['target_contract']}")
    print(f"mmn_adoption_boundary={reference['mmn_adoption_boundary']}")
    print(
        "next_memory_preview_mapping_review_required="
        f"{reference['next_memory_preview_mapping_review_required']}"
    )
    print(f"memory_write_authorized={flags['memory_write_authorized']}")
    print(f"persistent_memory_mutation_authorized={flags['persistent_memory_mutation_authorized']}")
    print(f"execution_payload_enabled={flags['execution_payload_enabled']}")

    assert reference["target_contract"] == "BiasAuditedSemanticFeatureViewContractV0"
    assert flags["memory_write_authorized"] is False
