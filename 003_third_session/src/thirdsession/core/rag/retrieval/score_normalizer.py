# 목적: 점수 정규화 전략을 제공한다.
# 설명: 거리 점수를 유사도 점수로 변환하거나 스케일을 맞춘다.
# 디자인 패턴: Strategy
# 참조: thirdsession/core/rag/retrieval/search_service.py

"""점수 정규화 모듈."""

from __future__ import annotations


class ScoreNormalizer:
    """점수 정규화기."""

    def distance_to_similarity(self, distance: float) -> float:
        """거리 점수를 유사도로 변환한다."""
        # TODO: 변환 수식과 예외 처리를 정의한다.
        raise NotImplementedError

    def min_max_scale(self, scores: list[float]) -> list[float]:
        """점수를 0~1 범위로 정규화한다."""
        # TODO: 최소/최대 스케일링 규칙을 구현한다.
        raise NotImplementedError
