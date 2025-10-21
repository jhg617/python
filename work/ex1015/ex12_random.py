import random

lotto = set()
while True:
    value = random.choice(range(1, 45)) # 1~44사이의 난수를 추출하여 value에 저장
    lotto.add(value) # 이미 저장된 값을 저장되지 않는다.
    if len(lotto) == 6:
        break # lotto의 길이가 6이 될때 탈출!
print("lotto:", lotto)