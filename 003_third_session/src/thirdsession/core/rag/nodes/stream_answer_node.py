# 목적: 답변 스트리밍을 수행한다.
# 설명: 토큰 단위 스트리밍 규칙을 담당한다.
# 디자인 패턴: Command
# 참조: thirdsession/api/rag/model/chat_stream_event.py

"""답변 스트리밍 노드 모듈."""

from __future__ import annotations

from collections.abc import AsyncIterator

# TODO: 스트리밍 이벤트 모델/타입을 활용하도록 연결한다.


class StreamAnswerNode:
    """답변 스트리밍 노드."""

    async def run(
        self,
        answer: str,
        trace_id: str,
        seq_start: int = 1,
        node: str | None = "stream_answer",
    ) -> AsyncIterator[str]:
        """답변을 스트리밍한다.

        Args:
            answer: 최종 답변 문자열.
            trace_id: 스트리밍 추적 식별자.
            seq_start: 시작 시퀀스 번호.
            node: 노드 식별자(선택).

        Yields:
            str: SSE 데이터 라인.
        """
        # TODO: answer를 토큰 단위로 분리해 SSE 이벤트를 생성한다.
        # TODO: seq 단조 증가와 trace_id 포함 규칙을 반영한다.
        _ = answer
        _ = trace_id
        _ = seq_start
        _ = node
        raise NotImplementedError("답변 스트리밍 로직을 구현해야 합니다.")

    def _split_answer(self, answer: str) -> list[str]:
        """답변을 토큰 단위로 분리한다."""
        # TODO: 토큰 분할 규칙(공백/문장/모델 토큰)을 확정한다.
        _ = answer
        raise NotImplementedError("토큰 분할 규칙을 구현해야 합니다.")
