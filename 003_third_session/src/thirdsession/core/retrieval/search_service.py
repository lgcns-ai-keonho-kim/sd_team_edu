# 목적: 검색 후처리와 결과 포맷을 담당한다.
# 설명: 거리/유사도 점수 해석 및 후처리 절차를 캡슐화한다.
# 디자인 패턴: Facade
# 참조: thirdsession/core/retrieval/vector_repository.py

"""검색 서비스 모듈."""

from __future__ import annotations

from typing import Sequence

from thirdsession.core.retrieval.document_model import DocumentModel
from thirdsession.core.retrieval.vector_repository import VectorRepository


class SearchService:
    """검색 서비스."""

    def __init__(self, repository: VectorRepository) -> None:
        self._repository = repository

    def search(self, query_vector: Sequence[float], top_k: int) -> list[DocumentModel]:
        """검색을 수행하고 후처리를 적용한다."""
        # TODO: 점수 임계값/중복 제거/정렬 규칙을 구현한다.
        raise NotImplementedError
