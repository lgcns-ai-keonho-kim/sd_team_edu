# 목적: LLM 기반 재정렬기를 정의한다.
# 설명: 질문과 문서를 입력으로 점수를 계산해 정렬한다.
# 디자인 패턴: Strategy
# 참조: thirdsession/core/rag/postprocessing/postprocess_pipeline.py

"""LLM 재정렬기 모듈."""

from __future__ import annotations

from typing import Any


class LlmReranker:
    """LLM 재정렬기."""

    def rerank(self, question: str, docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """LLM 기반으로 재정렬한다."""
        # TODO: LLM 점수 계산과 정렬 규칙을 구현한다.
        raise NotImplementedError
