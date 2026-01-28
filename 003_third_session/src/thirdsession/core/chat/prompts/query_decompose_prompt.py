# 목적: 쿼리 분해 프롬프트를 제공한다.
# 설명: 하위 질문 생성 규칙을 포함한 텍스트 템플릿이다.
# 디자인 패턴: Builder
# 참조: thirdsession/core/chat/nodes/query_decompose_node.py

"""쿼리 분해 프롬프트 모듈."""

from __future__ import annotations


class QueryDecomposePrompt:
    """쿼리 분해 프롬프트 생성기."""

    def build(self) -> str:
        """프롬프트 텍스트를 생성한다."""
        # TODO: 쿼리 분해 프롬프트 템플릿을 정의한다.
        raise NotImplementedError
