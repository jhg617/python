"""
[메세지]->[ChatPromptTemplate]->[ChatModel]->[StrOutputParser]->[결과]
"""
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import HumanMessagePromptTemplate
from langchain_core.prompts import SystemMessagePromptTemplate
from dotenv import load_dotenv

load_dotenv()

# 채팅모델 지정
chat_model = ChatAnthropic(model="claude-3-5-haiku-latest")
# 프롬프트 정의 - 시스템 메시지와 사용자메시지를 한번에 정의
chat_prompt_tmp = ChatPromptTemplate.from_messages(
    [
        SystemMessagePromptTemplate.from_template("당신은 까칠한 AI도우미입니다. 사용자의 질문에 최대 3줄로 답하세요."),
        HumanMessagePromptTemplate.from_template("{question}")
    ]
)
# 출력파서 정의
string_output_parser = StrOutputParser()

# 체인 연결
chain = chat_prompt_tmp|chat_model|string_output_parser

# 체인에 딕셔너리 입력
result = chain.invoke({"question":"파이썬에 리스트를 정렬하는 방법은?"})
print(result)