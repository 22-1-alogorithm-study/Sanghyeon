import math
import sys

input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))
new_k = [[] for _ in range(n)]


def find_prime(num):
    global idx
    for j in range(2, int(math.sqrt(num)+1)):
        if num % j == 0:
            new_k[idx].append(j)
            find_prime(num // j)
            return
        elif j == int(math.sqrt(num)):
            new_k[idx].append(num)
    if num <= int(math.sqrt(num)+2):
        new_k[idx].append(num)


idx = 0
for i in k:
    find_prime(i)
    idx += 1

for i in new_k:
    print(' '.join(map(str, i)))
