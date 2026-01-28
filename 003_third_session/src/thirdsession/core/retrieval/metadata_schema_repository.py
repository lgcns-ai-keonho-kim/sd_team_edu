# 목적: 메타데이터 키/값 스키마를 조회한다.
# 설명: 허용 목록 기반 필터 생성을 위한 조회 인터페이스다.
# 디자인 패턴: Repository
# 참조: thirdsession/core/retrieval/filter_expression_builder.py

"""메타데이터 스키마 리포지토리 모듈."""

from __future__ import annotations


class MetadataSchemaRepository:
    """메타데이터 스키마 리포지토리."""

    def fetch_schema(self) -> dict[str, dict[str, list[str]]]:
        """메타데이터 키/유니크 값을 조회한다."""
        # TODO: DB에서 메타데이터 키/값 목록을 조회하는 로직을 구현한다.
        raise NotImplementedError
