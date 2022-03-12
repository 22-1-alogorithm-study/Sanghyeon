n = int(input())
weight = []
for i in range(n):
    weight.append(int(input()))
weight.sort()


def function():
    max_weight = 0
    for j in range(len(weight)):
        temp = int(weight[j]) * (len(weight) - j)
        if temp > max_weight:
            max_weight = temp
        else:
            pass
    return max_weight


print(function())

