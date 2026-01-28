# 목적: 검색 대상 문서 모델을 정의한다.
# 설명: 콘텐츠와 메타데이터를 함께 관리하는 값 객체이다.
# 디자인 패턴: Value Object
# 참조: thirdsession/core/retrieval/vector_repository.py

"""문서 모델 모듈."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class DocumentModel:
    """문서 모델."""

    content: str
    metadata: dict[str, Any]

    def todo_validate(self) -> None:
        """문서 유효성 검증 자리표시자."""
        # TODO: 문서 필수 필드/길이/메타데이터 유효성 규칙을 정의한다.
        raise NotImplementedError
