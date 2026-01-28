# 목적: 검색 결과를 병합한다.
# 설명: 중복 제거 및 정규화 이후 병합을 수행한다.
# 디자인 패턴: Command
# 참조: thirdsession/core/postprocessing/postprocess_pipeline.py

"""결과 병합 노드 모듈."""

from __future__ import annotations

from typing import Any


class MergeNode:
    """결과 병합 노드."""

    def run(self, groups: list[list[Any]]) -> list[Any]:
        """검색 결과를 병합한다."""
        # TODO: 병합/정규화/중복 제거 규칙을 구현한다.
        raise NotImplementedError
