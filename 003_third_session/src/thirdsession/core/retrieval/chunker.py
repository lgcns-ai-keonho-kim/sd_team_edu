# 목적: 문서를 청크 단위로 분할한다.
# 설명: 청크 크기/오버랩 기준을 적용하는 분할기이다.
# 디자인 패턴: Factory Method
# 참조: thirdsession/core/retrieval/document_model.py

"""청크 분할기 모듈."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class Chunker:
    """청크 분할기."""

    chunk_size: int
    chunk_overlap: int

    def split(self, text: str) -> list[str]:
        """문서를 청크로 분할한다."""
        # TODO: 청크 분할 기준과 오버랩 규칙을 구현한다.
        raise NotImplementedError
