import pandas as pd

df = pd.read_csv("data/test_data.tsv", sep="\t") # 각 열이 탭으로 구분되었다
print(df)
print("---- 위쪽 2개의 데이터만 가져오자 ----")
print(df.head(2))
print("---- 아래쪽 2개의 데이터만 가져오자 ----")
print(df.tail(2))
print("---- 년도 컬럼만 가져오자 ----")
print(df['year'])