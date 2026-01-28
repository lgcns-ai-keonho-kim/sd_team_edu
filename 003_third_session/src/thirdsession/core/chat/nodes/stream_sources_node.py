# 목적: 근거 문서 스트리밍을 수행한다.
# 설명: 답변 이후 근거를 전송하는 규칙을 담당한다.
# 디자인 패턴: Command
# 참조: thirdsession/core/chat/nodes/stream_answer_node.py

"""근거 스트리밍 노드 모듈."""

from __future__ import annotations

from collections.abc import AsyncIterator
from typing import Any


class StreamSourcesNode:
    """근거 스트리밍 노드."""

    async def run(self, sources: list[Any]) -> AsyncIterator[str]:
        """근거 문서를 스트리밍한다."""
        # TODO: 근거 전송 규칙과 종료 이벤트를 구현한다.
        raise NotImplementedError
