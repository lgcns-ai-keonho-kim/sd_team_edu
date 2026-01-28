# 목적: 서비스 수준 RAG 파이프라인 그래프를 정의한다.
# 설명: 검색 → 필터 → 정규화 → 병합 → 후처리 → 생성 → 스트리밍 순서를 담는다.
# 디자인 패턴: State Machine
# 참조: thirdsession/core/chat/nodes/postprocess_node.py

"""RAG 파이프라인 그래프 모듈."""

from __future__ import annotations


class RagPipelineGraph:
    """RAG 파이프라인 그래프."""

    def build(self) -> None:
        """그래프를 구성한다."""
        # TODO: LangGraph 그래프와 노드 연결을 구현한다.
        raise NotImplementedError
