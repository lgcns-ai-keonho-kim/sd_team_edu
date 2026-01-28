# 목적: 애플리케이션 환경 설정을 정의한다.
# 설명: 환경 변수 기반 설정을 로딩하는 설정 객체이다.
# 디자인 패턴: Configuration Object
# 참조: thirdsession/main.py, thirdsession/core/chat/usecases/rag_chat_usecase.py

"""애플리케이션 설정 모듈."""

from __future__ import annotations

from dataclasses import dataclass
import os


@dataclass(frozen=True)
class AppConfig:
    """애플리케이션 설정."""

    openai_api_key: str | None
    google_api_key: str | None
    redis_url: str | None

    @classmethod
    def from_env(cls) -> "AppConfig":
        """환경 변수에서 설정을 로딩한다."""
        # TODO: dotenv 로딩과 필수 값 검증을 추가한다.
        raise NotImplementedError
