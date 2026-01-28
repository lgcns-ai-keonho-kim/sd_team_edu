# 목적: HyDE 생성 프롬프트를 제공한다.
# 설명: 가상 문서 생성 규칙을 포함한다.
# 디자인 패턴: Builder
# 참조: thirdsession/core/chat/nodes/hyde_node.py

"""HyDE 프롬프트 모듈."""

from __future__ import annotations


class HydePrompt:
    """HyDE 프롬프트 생성기."""

    def build(self) -> str:
        """프롬프트 텍스트를 생성한다."""
        # TODO: HyDE 프롬프트 템플릿을 정의한다.
        raise NotImplementedError
