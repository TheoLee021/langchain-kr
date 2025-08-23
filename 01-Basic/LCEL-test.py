from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

from langchain_teddynote import logging

logging.langsmith("CH01-Basic")

from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser

template = """
당신은 10년차 웹 개발자입니다. 주어진 상황에 맞는 웹 개발 코드를 작성해 주세요.
양식은 [FORMAT]을 참고하여 작성해 주세요.

#상황:
{question}

#FORMAT:
- 웹 개발 코드:
- 웹 개발 설명:
"""

# 프롬프트 템플릿을 이용하여 프롬프트를 생성합니다.
prompt = PromptTemplate.from_template(template)

# ChatOpenAI 챗모델을 초기화합니다.
model = ChatOpenAI(model_name="gpt-4o-mini")

# 문자열 출력 파서를 초기화합니다.
output_parser = StrOutputParser()

chain = prompt | model | output_parser

# 체인을 실행하고 결과를 출력합니다.
result = chain.invoke({"question": "미국에서 병원가기"})
print(result)