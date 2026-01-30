# 목적: 검색 결과를 검증한다.
# 설명: 문서 관련성 여부를 판단하는 노드이다.
# 디자인 패턴: Command
# 참조: thirdsession/core/rag/prompts/verify_prompt.py

"""검색 검증 노드 모듈."""

from __future__ import annotations

from typing import Any

from thirdsession.core.common.llm_client import LlmClient


class VerifyNode:
    """검색 검증 노드."""

    def __init__(self, llm_client: LlmClient | None = None) -> None:
        """노드 의존성을 초기화한다.

        Args:
            llm_client: LLM 클라이언트(선택).
        """
        self._llm_client = llm_client

    def run(self, question: str, docs: list[Any]) -> list[Any]:
        """관련 문서만 선택한다."""
        # TODO: LLM 검증 로직과 필터링 기준을 구현한다.
        _ = self._llm_client
        raise NotImplementedError
