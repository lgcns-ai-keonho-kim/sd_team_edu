# 목적: 검색을 수행하는 노드를 정의한다.
# 설명: 리트리버/벡터 스토어를 호출해 후보 문서를 수집한다.
# 디자인 패턴: Command
# 참조: thirdsession/core/rag/retrieval/search_service.py

"""검색 노드 모듈."""

from __future__ import annotations

from typing import Any


class SearchNode:
    """검색 노드."""

    def run(self, query: str, retriever: Any) -> list[Any]:
        """쿼리를 검색해 문서를 반환한다."""
        # TODO: 리트리버 호출과 예외 처리를 구현한다.
        raise NotImplementedError
