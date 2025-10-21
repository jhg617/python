"""
[결과]
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""

for i in range(1, 4): # 3번 반복
    msg = ""
    for j in range(1, 6): # 1~5까지 반복
        msg += "{}\t".format(j)
        if j == 3:
            break; # j가 3일때 탈출
    print(msg)
    