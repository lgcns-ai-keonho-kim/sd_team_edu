# 목적: 메타데이터 필터 정책을 정의한다.
# 설명: 권한/언어/기간 등 필수 조건을 강제한다.
# 디자인 패턴: Policy
# 참조: thirdsession/core/rag/retrieval/search_service.py

"""메타데이터 필터 모듈."""

from __future__ import annotations

from typing import Any

from thirdsession.core.rag.retrieval.document_model import DocumentModel


class MetadataFilterPolicy:
    """메타데이터 필터 정책."""

    def apply(self, documents: list[DocumentModel], context: dict[str, Any]) -> list[DocumentModel]:
        """메타데이터 필터를 적용한다."""
        # TODO: 권한/언어/버전 필터 규칙을 구현한다.
        raise NotImplementedError
