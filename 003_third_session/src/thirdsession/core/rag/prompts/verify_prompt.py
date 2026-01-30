# 목적: 검색 결과 검증 프롬프트를 제공한다.
# 설명: 문서 관련성 판단 규칙을 포함하며 싱글턴으로 관리한다.
# 디자인 패턴: Singleton
# 참조: thirdsession/core/rag/nodes/verify_node.py

"""검색 검증 프롬프트 모듈."""

from textwrap import dedent

from langchain_core.prompts import PromptTemplate

_VERIFY_PROMPT = dedent(
    """\
You are a verifier. Decide if the document is relevant to the user's question.

[Question]
{question}

[Document]
{document}

[Rules]
- Answer with exactly one label: YES or NO.
- YES if the document directly helps answer the question.
- NO if it is unrelated or too vague.

[Output]
YES|NO
"""
)

VERIFY_PROMPT = PromptTemplate(
    template=_VERIFY_PROMPT,
    input_variables=["question", "document"],
)
