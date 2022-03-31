import sys, itertools
input = sys.stdin.readline

question = int(input())
number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
num = list(itertools.permutations(number, 3))
remove = 0
print(len(num))
for _ in range(question):
    prd, st, bl = map(int, input().split())
    prd = list(str(prd))
    remove = 0
    for i in range(len(num)):
        strike = ball = 0
        i -= remove
        for j in range(3):
            if prd[j] == num[i][j]:
                strike += 1
            elif prd[j] in num[i]:
                ball += 1

        if strike != st or ball != bl:
            num.remove(num[i])
            remove += 1
print(len(num))
