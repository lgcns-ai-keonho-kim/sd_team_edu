# 목적: RAG 후처리 파이프라인을 정의한다.
# 설명: 정책 필터, 중복 제거, LLM 재정렬, 압축 순서를 관리한다.
# 디자인 패턴: Pipeline
# 참조: thirdsession/core/rag/retrieval/metadata_filter.py, thirdsession/core/rag/postprocessing/llm_reranker.py

"""후처리 파이프라인 모듈."""

from __future__ import annotations

from typing import Any


class PostprocessPipeline:
    """후처리 파이프라인."""

    def run(self, docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """후처리 파이프라인을 실행한다."""
        # TODO: 정책 필터/중복 제거/다양성/재정렬/압축을 구현한다.
        raise NotImplementedError
