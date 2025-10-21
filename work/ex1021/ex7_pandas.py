import pandas as pd
from pandas import Series, DataFrame

ko = pd.Series([96200,92450,95456,92300])
print(ko)
print("--------- index값 변경 ---------")
ko = Series([96200,92450,95456,92300], 
            index=['10-02', '10-03', '10-04', '10-05'])
print(ko)
print("--------- index값들만 출력 ---------")
for day in ko.index:
    print(day) # index들만 출력
print("--------- value들만 출력 ---------")
for price in ko.values:
    print(price) # 값들만 출력