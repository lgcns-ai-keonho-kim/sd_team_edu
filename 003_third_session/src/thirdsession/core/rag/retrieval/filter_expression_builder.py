# 목적: 메타데이터 필터 표현식을 구성한다.
# 설명: 정책/컨텍스트를 검색 엔진 조건으로 변환한다.
# 디자인 패턴: Builder
# 참조: thirdsession/core/rag/retrieval/metadata_filter.py

"""필터 표현식 빌더 모듈."""

from __future__ import annotations

from typing import Any


class FilterExpressionBuilder:
    """필터 표현식 빌더."""

    def build(self, context: dict[str, Any]) -> dict[str, Any]:
        """필터 표현식을 생성한다."""
        # TODO: 필수/선택 조건을 분리해 표현식을 구성한다.
        raise NotImplementedError
