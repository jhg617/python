import os

cpath = os.getcwd() # 현재 소스파일의 위치 값
print("현재 위치:", cpath)
print("----------------")
sub_list = os.listdir(cpath)
for s in sub_list:
    print(s)