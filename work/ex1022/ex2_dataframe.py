from pandas import Series, DataFrame
# 데이터들만
emp = [[100, "마루치", "dev"],
    [220, "아라치", "dev"],
    [250, "마동탁", "dev"],
    [217, "이도", "CEO"]]

# 컬럼명만 따로 저장하자
c_name = ["empno", "ename", "job"]

# 위의 내용들을 가지고 DataFrame 생성
df = DataFrame.from_records(emp, columns=c_name)
print(df)
"""
이쯤에서 정리해보면 DataFrame을 두 번에 걸쳐 만들어 봤다.
 - 딕셔너리를 가지고 DataFrame생성 시 바로 넣어 만드는 법
 - 리스트로 된 데이터와 컬러명을 가지고 DataFrame을 만드는 법
"""
print("--------- df.loc[1] --------")
print(df.loc[1]) # 1 : 인덱스가 1인 행의 정보를 출력함!

print("--------- 특정 행에서 특정 행까지(범위 설정) --------")
print(df.loc[1:3])
print("-----------------")
print(df[1:3]) # 1에서 3번지 전까지 출력
print("-------- 조건부여(사번이 250번 이상) ---------")
print(df[df.empno >= 250])
print("-------- 조건부여(사번이 220번 이상이고 직종이 dev인 사원) ---------")
print(df[(df.empno >= 220) & (df.job == "dev")])

"""
지금까지는 DataFrame의 행을 선택하는 법을 했다.
지금부터는 열을 선택해 보자!
"""
print("----- 열 선택 -----")
print(df["ename"]) # 이름이라는 열을 선택하여 출력함
print("----- 다중 열 선택 -----")
print(df[["ename", "job"]]) # 대괄호를 하나 더 사용해야 함
print("--------------")
print(df)
print("-------모든 행을 포함하고, 열을 첫번째와 두번째만 출력-------")
print(df.iloc[: , 0:2]) # iloc[행범위 , 열범위]