# 목적: 검색 결과를 검증한다.
# 설명: 문서 관련성 여부를 판단하는 노드이다.
# 디자인 패턴: Command
# 참조: thirdsession/core/chat/prompts/verify_prompt.py

"""검색 검증 노드 모듈."""

from __future__ import annotations

from typing import Any


class VerifyNode:
    """검색 검증 노드."""

    def run(self, question: str, docs: list[Any]) -> list[Any]:
        """관련 문서만 선택한다."""
        # TODO: LLM 검증 로직과 필터링 기준을 구현한다.
        raise NotImplementedError
