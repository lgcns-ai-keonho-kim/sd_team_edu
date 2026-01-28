# thirdsession

이 프로젝트는 FastAPI 기반의 기본 애플리케이션 진입점을 제공합니다.

## 실행 방법

아래 두 가지 방식 중 하나로 실행할 수 있습니다.

### 1) uvicorn CLI 방식 (권장)

```txt
uv run uvicorn thirdsession.main:app --host 0.0.0.0 --port 8000 --reload
```

### 2) 모듈 직접 실행 방식

```txt
uv run python -m thirdsession.main
```

## 기본 엔드포인트

- 헬스 체크: `GET /health`

## 주요 위치

- 애플리케이션 진입점: `src/thirdsession/main.py`
- API 영역: `src/thirdsession/api`
- Core 영역: `src/thirdsession/core`

## 학습 구현 가이드

- 이 프로젝트는 교육생이 단계별로 TODO를 채우는 방식으로 설계되어 있습니다.
- TODO 위치는 모두 `NotImplementedError`를 발생시키므로, 단계별 구현이 필요합니다.

## 환경 설정

프로젝트 루트에서 아래 순서로 실행하세요.

```txt
uv venv .venv
uv sync
```
