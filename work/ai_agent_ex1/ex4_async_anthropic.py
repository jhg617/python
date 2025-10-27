import asyncio
import os
from anthropic import AsyncAnthropic
from dotenv import load_dotenv

# .env파일 로드
load_dotenv()

# 원하는 값을 가져오기
api_key = os.getenv("ANTHROPIC_API_KEY")
if not api_key:
    raise ValueError("ANTHROPIC_API_KEY가 설정되지 않았음!") # JAVA의 Throws와 같다. (의도적으로 예외 발생)

# 비동기 클라이언트 생성
# client = anthropic.Anthropic(api_key=api_key) # 지난 시간에 생성된 객체
claude_client = AsyncAnthropic(api_key=api_key)

async def call_claude(promt:str, model:str = "claude-3-5-haiku-latest") -> str:
    # Claude API를 비동기식으로 호출
    async with AsyncAnthropic(api_key=api_key) as client:
        response = await client.messages.create(
            model=model,
            messages=[{"role":"user", "content":promt}],
            max_tokens=1000,
        )
    return response.content[0].text

async def main():
    prompt = "비동기 프로그래밍에 대해 두 세문장으로 설명해 주세요"
    result = await call_claude(prompt)
    print(result)
    
if __name__ == "__main__":
    # Windows asyncio 에러 방지
    import sys
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio._WindowsProactorEventLoopPolicy())
    asyncio.run(main())