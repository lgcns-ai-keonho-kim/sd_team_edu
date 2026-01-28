# 목적: 답변 스트리밍을 수행한다.
# 설명: 토큰 단위 스트리밍 규칙을 담당한다.
# 디자인 패턴: Command
# 참조: thirdsession/core/chat/nodes/generate_node.py

"""답변 스트리밍 노드 모듈."""

from __future__ import annotations

from collections.abc import AsyncIterator


class StreamAnswerNode:
    """답변 스트리밍 노드."""

    async def run(self, answer: str) -> AsyncIterator[str]:
        """답변을 스트리밍한다."""
        # TODO: 스트리밍 전송 규칙과 종료 이벤트를 구현한다.
        raise NotImplementedError
