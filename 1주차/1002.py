import math

# 입력
t = int(input())
p = []  # 출력할 값을 담는 배열.

for i in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    # 두 점 사이 거리 계산.
    r3 = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    long = max(r1, r2)
    short = min(r1, r2)

    if r3 == 0 and r1 == r2:
        p.append(-1)
    elif r3 >= long:  # 외접하는 경우
        if r3 == r1 + r2:
            p.append(1)
        elif r3 > r1 + r2:
            p.append(0)
        elif r3 < r1 + r2:
            p.append(2)
    elif r3 < long:  # 내접하는 경우
        if r3 > long - short:
            p.append(2)
        elif r3 == long - short:
            p.append(1)
        elif r3 < long - short:
            p.append(0)

for i in p:
    print(i)
