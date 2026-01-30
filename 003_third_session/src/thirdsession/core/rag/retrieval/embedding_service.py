# 목적: 텍스트를 임베딩 벡터로 변환한다.
# 설명: 임베딩 모델 호출 로직을 캡슐화한다.
# 디자인 패턴: Service
# 참조: thirdsession/core/rag/retrieval/vector_repository.py

"""임베딩 서비스 모듈."""

from __future__ import annotations

from typing import Sequence


class EmbeddingService:
    """임베딩 서비스."""

    def __init__(self, model_name: str) -> None:
        self._model_name = model_name

    def embed(self, texts: Sequence[str]) -> list[list[float]]:
        """텍스트 목록을 임베딩 벡터로 변환한다."""
        # TODO: 임베딩 API 호출 및 배치 처리 로직을 구현한다.
        raise NotImplementedError
