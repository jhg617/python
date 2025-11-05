"""
벡터스토어를 활용하는 간단한 예제
pip install python-dotenv
pip install tenacity==8.2.3
pip install anthropic==0.49.0
pip install "fastapi[standard]"
pip install python-multipart unicorn
pip install lanchain[openai]==0.3.27
pip install lanchain[anthropic]==0.3.27
pip install pydantic
pip install protobuf
pip install chromadb
"""
import chromadb

# 클라이언트 생성
client = chromadb.Client()
collection = client.create_collection("my_db") # DB(스키마)생성

# 문서 추가 - 문서내용을 TEXT로 변환해서 저장해야함
collection.add(
    documents=["파이썬은 프로그래밍 언어", "머신러닝은 인공지능기술"],
    ids=["doc1", "doc2"],
)

# 검색
results = collection.query(query_texts=["프로그래밍"], n_results=3)
print(results["documents"])