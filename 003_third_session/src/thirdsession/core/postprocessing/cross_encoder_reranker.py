# 목적: Cross-Encoder 기반 재정렬기를 정의한다.
# 설명: 질문-문서 쌍 점수로 재정렬한다.
# 디자인 패턴: Strategy
# 참조: thirdsession/core/postprocessing/postprocess_pipeline.py

"""Cross-Encoder 재정렬기 모듈."""

from __future__ import annotations

from typing import Any


class CrossEncoderReranker:
    """Cross-Encoder 재정렬기."""

    def rerank(self, question: str, docs: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Cross-Encoder 점수로 재정렬한다."""
        # TODO: Cross-Encoder 모델 호출 및 정렬 규칙을 구현한다.
        raise NotImplementedError
