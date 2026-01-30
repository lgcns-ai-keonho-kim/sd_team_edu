# 목적: 대화 내역을 누적한다.
# 설명: user/assistant 메시지를 history에 추가한다.
# 디자인 패턴: Command
# 참조: thirdsession/core/rag/state/chat_state.py

"""대화 내역 누적 노드 모듈."""

from __future__ import annotations

from typing import Any


class AppendHistoryNode:
    """대화 내역 누적 노드."""

    def run(
        self,
        history: list[dict[str, Any]],
        user_message: str,
        assistant_message: str,
    ) -> list[dict[str, Any]]:
        """대화 내역을 누적한다."""
        updated = list(history)
        updated.append({"role": "user", "content": user_message})
        updated.append({"role": "assistant", "content": assistant_message})
        return updated
