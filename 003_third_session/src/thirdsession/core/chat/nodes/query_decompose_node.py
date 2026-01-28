# 목적: 질문을 하위 쿼리로 분해한다.
# 설명: 쿼리 분해 프롬프트를 이용하는 노드이다.
# 디자인 패턴: Command
# 참조: thirdsession/core/chat/prompts/query_decompose_prompt.py

"""쿼리 분해 노드 모듈."""

from __future__ import annotations


class QueryDecomposeNode:
    """쿼리 분해 노드."""

    def run(self, question: str) -> list[str]:
        """질문을 하위 쿼리로 분해한다."""
        # TODO: LLM 호출과 파싱 로직을 구현한다.
        raise NotImplementedError
