# 목적: rag_chat 핵심 유스케이스를 제공한다.
# 설명: 검색/후처리/생성 파이프라인을 실행하는 진입점이다.
# 디자인 패턴: Application Service
# 참조: thirdsession/core/common/app_config.py

"""rag_chat 유스케이스 모듈."""

from __future__ import annotations

from typing import Any

from thirdsession.core.common.app_config import AppConfig


class RagChatUseCase:
    """rag_chat 유스케이스."""

    def __init__(self, config: AppConfig) -> None:
        self._config = config

    def run(
        self,
        question: str,
        user_id: str | None,
        metadata: dict[str, Any] | None,
    ) -> dict[str, Any]:
        """rag_chat 유스케이스를 실행한다.

        Args:
            question: 사용자 질문.
            user_id: 사용자 식별자(선택).
            metadata: 추가 메타데이터(선택).

        Returns:
            dict[str, Any]: 답변/근거/추적 정보.
        """
        # TODO: RAG 파이프라인을 구성하고 실행한다.
        # TODO: 리트리버/벡터 스토어 인스턴스를 주입받도록 구조를 확장한다.
        # TODO: 프롬프트/후처리/생성 단계를 분리된 노드로 구성한다.
        _ = user_id
        _ = metadata
        raise NotImplementedError
