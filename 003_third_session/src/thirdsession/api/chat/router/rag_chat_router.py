# 목적: rag_chat 엔드포인트 라우터를 제공한다.
# 설명: FastAPI 라우터를 생성하고 서비스 호출을 연결한다.
# 디자인 패턴: Factory Method
# 참조: thirdsession/api/chat/service/rag_chat_service.py

"""rag_chat 라우터 모듈."""

from __future__ import annotations

from fastapi import APIRouter

from thirdsession.api.chat.model.rag_chat_request import RagChatRequest
from thirdsession.api.chat.model.rag_chat_response import RagChatResponse
from thirdsession.api.chat.service.rag_chat_service import RagChatService


def create_rag_chat_router(service: RagChatService) -> APIRouter:
    """rag_chat 라우터를 생성한다.

    Args:
        service: rag_chat 서비스.

    Returns:
        APIRouter: 구성된 라우터.
    """
    router = APIRouter(tags=["rag"])

    @router.post("/rag_chat", response_model=RagChatResponse)
    def rag_chat(request: RagChatRequest) -> RagChatResponse:
        """rag_chat 요청을 처리한다."""
        # TODO: 인증/권한 확인, 요청 유효성 검사를 강화한다.
        raise NotImplementedError

    @router.post("/rag_chat/stream")
    def rag_chat_stream(request: RagChatRequest) -> None:
        """rag_chat 스트리밍 요청을 처리한다."""
        # TODO: SSE 또는 스트리밍 응답 전송을 구현한다.
        raise NotImplementedError

    return router
