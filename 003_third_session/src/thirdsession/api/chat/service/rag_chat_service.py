# 목적: rag_chat 서비스 유스케이스 호출을 담당한다.
# 설명: API 계층에서 코어 유스케이스를 호출하고 응답 모델로 변환한다.
# 디자인 패턴: Service
# 참조: thirdsession/core/chat/usecases/rag_chat_usecase.py

"""rag_chat 서비스 모듈."""

from __future__ import annotations

from thirdsession.api.chat.model.rag_chat_request import RagChatRequest
from thirdsession.api.chat.model.rag_chat_response import RagChatResponse
from thirdsession.core.chat.usecases.rag_chat_usecase import RagChatUseCase


class RagChatService:
    """rag_chat 서비스 클래스."""

    def __init__(self, usecase: RagChatUseCase) -> None:
        self._usecase = usecase

    def handle(self, request: RagChatRequest) -> RagChatResponse:
        """rag_chat 요청을 처리한다.

        Args:
            request: rag_chat 요청 모델.

        Returns:
            RagChatResponse: 응답 모델.
        """
        # TODO: 예외 처리/로깅/메트릭 수집을 추가한다.
        raise NotImplementedError
