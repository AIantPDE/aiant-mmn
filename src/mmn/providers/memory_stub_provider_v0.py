from __future__ import annotations

from mmn.contracts.memory_preview_output_v0 import (
    MemoryPreviewOutputV0,
    build_memory_preview_output_v0,
)
from mmn.contracts.memory_record_v0 import build_memory_record_v0


class MemoryStubProviderV0:
    provider_name = "memory_stub_provider_v0"
    provider_version = "0.1.0"

    def generate(
        self,
        *,
        output_seed: str,
        richer_memory: bool = False,
    ) -> MemoryPreviewOutputV0:
        note_record = build_memory_record_v0(
            record_seed=f"{output_seed}::note",
            record_kind="summary_note",
            record_text="preview memory note",
            reason_codes=("MEMORY_STUB",),
        )
        citation_record = build_memory_record_v0(
            record_seed=f"{output_seed}::citation",
            record_kind="citation_note",
            record_text="preview citation note",
            reason_codes=("MEMORY_STUB",),
        )

        memory_strength_hint = "strong" if richer_memory else "medium"
        citation_hint = "available" if richer_memory else "limited"
        reason_codes = ("MEMORY_STUB", "RICHER_MEMORY") if richer_memory else ("MEMORY_STUB",)

        return build_memory_preview_output_v0(
            output_seed=output_seed,
            records=(note_record, citation_record),
            memory_strength_hint=memory_strength_hint,
            citation_hint=citation_hint,
            reason_codes=reason_codes,
        )
