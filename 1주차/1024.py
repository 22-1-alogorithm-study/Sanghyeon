n, l = map(int, input().split())

seq = []
while l <= 100:
    mid_term = n / l  # 중간 항 계산.
    if l % 2 == 0 and mid_term - int(mid_term) == 0.5:
        # l이 짝수이고 중간항이 X.5일 때 조건.
        num = (l // 2) - 0.5
        a = mid_term - num  # 첫째항
        if a < 0:
            l = -1
            break
        for i in range(l):
            seq.append(int(a))
            a += 1
        if sum(seq) == n:
            break
        else:
            seq = []
            l += 1
    elif l % 2 == 1 and mid_term - int(mid_term) == 0:
        # l이 홀수이고 중간항이 정수일 때 조건.
        num = (l - 1) // 2
        a = mid_term - num
        if a < 0:
            l = -1
            break
        for i in range(l):
            seq.append(int(a))
            a += 1
        if sum(seq) == n:
            break
        else:
            seq = []
            l += 1
    # elif mid_term - int(mid_term) != 0.5 or mid_term - int(mid_term) != 0:
    else:
        # 등차수열이 존재하지 않음.
        l += 1

if l < 2 or l > 100:
    print(-1)
else:
    for i in range(len(seq)):
        print(seq[i], end=' ')
