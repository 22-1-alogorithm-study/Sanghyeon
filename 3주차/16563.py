import sys
input = sys.stdin.readline

n = int(input())
k = list(map(int, input().split()))
new_k = [[] for _ in range(n)]
prime = []
idx = 0


def find_prime(n):
    sieve = [True] * n
    m = int(n ** 0.5)
    for i in range(2, m+1):
        if sieve[i] is True:
            for j in range(i+i, n, i):
                sieve[j] = False

    global prime
    prime = [i for i in range(2, n) if sieve[i] is True]


find_prime(max(k))

print(new_k)





