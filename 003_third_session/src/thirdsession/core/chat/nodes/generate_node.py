# 목적: 근거 기반 답변을 생성한다.
# 설명: 컨텍스트와 질문을 입력으로 답변을 만든다.
# 디자인 패턴: Command
# 참조: thirdsession/core/chat/prompts/answer_prompt.py

"""답변 생성 노드 모듈."""

from __future__ import annotations

from typing import Any


class GenerateNode:
    """답변 생성 노드."""

    def run(self, question: str, contexts: list[Any]) -> str:
        """근거 기반 답변을 생성한다."""
        # TODO: LLM 호출과 출력 포맷 규칙을 구현한다.
        raise NotImplementedError
