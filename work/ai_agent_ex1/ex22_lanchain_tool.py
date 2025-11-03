"""
LLM은 매우 똑똑하지만 모든 지식을 글로만 배운 친구다. 이 친구가
지난 몇년동안 가장 많이 사용하고 학습한 도구가 DB와 WebBrowser다.
랭체인에서는 보다 편리하게 도구를 LLM과 연계할 수 있도록
기능을 제공한다. 다음의 4단계로 구현한다.
1. 도구생성 : LLM이 사용할 도구를 준비하는 단계
2. 도구연결 : LLM에게 도구를 연결(Binding)하는 단계
3. 도구호출 : LLM이 사용할 도구를 선택하는 단계
4. 도구실행 : 실제로 LLM이 도구를 실행하고 작업하는 단계

- @tool 어노테이션(데코레이터)를 사용한 도구생성
"""
import random
from langchain.tools import tool
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("ANTHROPIC_API_KEY")

# 가위,바위,보 게임을 위한 Tool정의
@tool
def rock_paper_scissors() -> str:
    """ 가위,바위,보 중 하나를 랜덤하게 선택 """
    return random.choice(['가위','바위','보'])

# Tool이 바인딩된 LLM지정
llm = ChatAnthropic(model="claude-3-5-haiku-latest").bind_tools([rock_paper_scissors])

llm_chat = ChatAnthropic(model="claude-3-5-haiku-latest") # 해설용LLM

print(llm) # llm이 tool을 binding했는지 확인!

# 승부판정
def judge(user_choise, computer_choice):
    """ 가위, 바위, 보 승패를 판정합니다. """
    user_choice = user_choise.strip()
    computer_choice = computer_choice.strip()
    if user_choice == computer_choice:
        return "무승부"
    elif (user_choice, computer_choice) in [
        ("가위", "보"),
        ("바위", "가위"),
        ("보", "바위")
    ]:
        return "사용자가 이겼습니다!"
    else:
        return "패배"
    
# 게임 루프
print("가위,바위,보 (종료:q)")
while (user_input := input("\n가위,바위,보 :")) != "q" :
    # LLM에게 tool 호출
    ai_msg = llm.invoke(f"가위,바위,보 게임: 사용자가 {user_input}를 냈습니다. rock_paper_scissors tool을 사용하세요")
    
    # tool호출 확인 및 실행
    if ai_msg.tool_calls:
        print(type(rock_paper_scissors))
        llm_choice = rock_paper_scissors.invoke("") # tool 호출
        print(f"LLM이 선택한 도구: {llm_choice}")
        result = judge(user_input, llm_choice)
        
        print(f"승부: {result}")
    
        # 결과를 해설응답 생성
        final = llm_chat.invoke(
            f"가위,바위,보 게임 결과를 재미있게 해설해 주세요! : 사용자: {user_input}, AI: {llm_choice}, 결과: 사용자의 {result}"
        )
        print(final) # 결과 구조 확인
        print(f"    - LLM해설: {final.content}")
        print(f"게임 요약: 유저({user_input}) VS AI({llm_choice}) => {result}")
    else:
        print("Tool호출 실패")