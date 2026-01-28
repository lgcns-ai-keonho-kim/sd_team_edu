# 목적: 하이브리드 검색 결합 전략을 정의한다.
# 설명: 점수 결합/순위 결합 방식 선택을 담당한다.
# 디자인 패턴: Strategy
# 참조: thirdsession/core/retrieval/score_normalizer.py

"""하이브리드 결합 전략 모듈."""

from __future__ import annotations


class HybridFusionStrategy:
    """하이브리드 결합 전략."""

    def fuse(self, vector_scores: list[float], keyword_scores: list[float]) -> list[float]:
        """벡터/키워드 점수를 결합한다."""
        # TODO: 가중합/RRF/재정렬 결합 방식을 구현한다.
        raise NotImplementedError
