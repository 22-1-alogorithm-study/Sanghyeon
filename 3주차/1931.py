import sys
input = sys.stdin.readline
n = int(input())
a = 0
info = [[] for _ in range(n)]
for i in range(n):
    s, e = map(int, input().split())
    info[i].append(s)
    info[i].append(e)
info = sorted(info, key=lambda a: a[0])  # 시작 시간 기준 정렬.
info = sorted(info, key=lambda a: a[1])  # 종료 시간 기준 정렬.

count = 0
end = 0
for i in range(n):
    if info[i][0] >= end:
        count += 1
        end = info[i][1]

print(count)

