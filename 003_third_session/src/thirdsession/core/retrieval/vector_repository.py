# 목적: 벡터 저장/검색 리포지토리를 정의한다.
# 설명: PGVector 등 벡터 DB와의 입출력 계약을 담당한다.
# 디자인 패턴: Repository
# 참조: thirdsession/core/retrieval/document_model.py

"""벡터 리포지토리 모듈."""

from __future__ import annotations

from typing import Sequence

from thirdsession.core.retrieval.document_model import DocumentModel


class VectorRepository:
    """벡터 리포지토리."""

    def save(self, document: DocumentModel, embedding: Sequence[float]) -> None:
        """문서와 임베딩을 저장한다."""
        # TODO: 저장소 스키마와 저장 로직을 구현한다.
        raise NotImplementedError

    def search(self, query_vector: Sequence[float], top_k: int) -> list[DocumentModel]:
        """쿼리 벡터로 유사 문서를 검색한다."""
        # TODO: 검색 쿼리/정렬/필터 로직을 구현한다.
        raise NotImplementedError
