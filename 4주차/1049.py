import sys

input = sys.stdin.readline

n, m = map(int, input().split())
pack_list, ind_list = [], []


def min_payment(p, ind):
    global n
    num1 = n // 6
    num2 = n % 6
    if num2 * ind >= p:
        return p*(num1+1)
    elif ind * 6 < p:
        return n * ind
    else:
        return num1 * p + num2 * ind


for i in range(m):
    pack, individual = map(int, input().split())
    pack_list.append(pack)
    ind_list.append(individual)

result = min_payment(min(pack_list), min(ind_list))
print(result)

