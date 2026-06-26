# ruff: noqa: E501
from __future__ import annotations

from pathlib import Path

DOC_ROOT = Path("docs/authority_event_memory")

DOCS = [
    DOC_ROOT / "MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_CURRENT_BUSINESS_INTENT_V0.md",
    DOC_ROOT / "MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_LEGACY_SEAM_ALIGNMENT_V0.md",
    DOC_ROOT / "MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_COMPATIBILITY_BOUNDARY_V0.md",
    DOC_ROOT / "MMN_AUTHORITY_EVENT_MEMORY_V1_3_1_ENGINEERING_ENTRY_PLAN_V0.md",
]


def _read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def test_authority_event_memory_v1_3_1_docs_exist() -> None:
    for path in DOCS:
        assert path.exists(), path


def test_authority_event_memory_v1_3_1_current_intent_markers() -> None:
    text = _read(DOCS[0])
    required_markers = [
        "V1.3.1 defines the current MMN authority event memory intent",
        "Existing V0 preview/writeback/memory seams are legacy-compatible host surfaces only",
        "MMNEventMemoryRecordV1",
        "AuditEvidenceDigestV1",
        "MemoryPromotionChecklistV1",
        "AttributionScoringPolicyV1",
        "AttributionMultiplicityControlV1",
        "non-executing only",
        "LIVE_BUY",
        "LIVE_SELL",
        "EXECUTION_AUTHORIZED",
    ]
    for marker in required_markers:
        assert marker in text


def test_authority_event_memory_v1_3_1_legacy_seam_boundary_markers() -> None:
    text = _read(DOCS[1])
    required_markers = [
        "MEMORY_PREVIEW_OUTPUT_V0",
        "MEMORY_RECORD_V0",
        "MEMORY_WRITEBACK_REQUEST_V0",
        "MEMORY_WRITEBACK_RECORD_V0",
        "MMN_OBJECT_FAMILY_V0",
        "MMN_FIXTURE_STRATEGY_V0",
        "V0 provides host-seam compatibility",
        "V1.3.1 provides current authority event memory intent",
        "aiant-contracts will provide schema truth",
    ]
    for marker in required_markers:
        assert marker in text


def test_authority_event_memory_v1_3_1_forbidden_boundary_markers() -> None:
    text = _read(DOCS[2])
    required_markers = [
        "No MMN memory object",
        "opportunity memory says buy",
        "risk memory says sell",
        "writeback grants persistence",
        "validator pass means causal proof",
        "no_schema_authority",
    ]
    for marker in required_markers:
        assert marker in text


def test_authority_event_memory_v1_3_1_engineering_entry_is_docs_test_only() -> None:
    text = _read(DOCS[3])
    required_markers = [
        "docs/test-only",
        "does not introduce",
        "real validators",
        "persistence layer",
        "event crawler",
        "live ingestion",
        "DRL bridge",
        "trading signal",
        "contracts object skeleton",
    ]
    for marker in required_markers:
        assert marker in text
