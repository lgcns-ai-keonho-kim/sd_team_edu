# 목적: 근거 기반 답변을 생성한다.
# 설명: 컨텍스트와 질문을 입력으로 답변을 만든다.
# 디자인 패턴: Command
# 참조: thirdsession/core/rag/prompts/answer_prompt.py

"""답변 생성 노드 모듈."""

from __future__ import annotations

from typing import Any

from thirdsession.core.common.llm_client import LlmClient
# TODO: 답변 프롬프트/포맷터를 연결한다.


class GenerateNode:
    """답변 생성 노드."""

    def __init__(self, llm_client: LlmClient | None = None) -> None:
        """노드 의존성을 초기화한다.

        Args:
            llm_client: LLM 클라이언트(선택).
        """
        self._llm_client = llm_client

    def run(self, question: str, contexts: list[Any]) -> str:
        """근거 기반 답변을 생성한다."""
        # TODO: LLM 호출과 출력 포맷 규칙을 구현한다.
        _ = question
        _ = contexts
        _ = self._llm_client
        raise NotImplementedError("답변 생성 로직을 구현해야 합니다.")

    def _format_contexts(self, contexts: list[Any]) -> str:
        """컨텍스트 목록을 LLM 입력 문자열로 변환한다."""
        # TODO: 컨텍스트 포맷 규칙을 확정한다.
        _ = contexts
        raise NotImplementedError("컨텍스트 포맷 규칙을 구현해야 합니다.")
