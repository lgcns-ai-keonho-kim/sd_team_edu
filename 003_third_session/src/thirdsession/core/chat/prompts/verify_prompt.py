# 목적: 검색 결과 검증 프롬프트를 제공한다.
# 설명: 문서 관련성 판단 규칙을 포함한다.
# 디자인 패턴: Builder
# 참조: thirdsession/core/chat/nodes/verify_node.py

"""검색 검증 프롬프트 모듈."""

from __future__ import annotations


class VerifyPrompt:
    """검색 검증 프롬프트 생성기."""

    def build(self) -> str:
        """프롬프트 텍스트를 생성한다."""
        # TODO: 검색 검증 프롬프트 템플릿을 정의한다.
        raise NotImplementedError
