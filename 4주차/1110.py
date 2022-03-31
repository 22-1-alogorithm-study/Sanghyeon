import sys
input = sys.stdin.readline

n = int(input())
arr_n = str(n)
new_num, cycle = -1, 0

if len(arr_n) == 1:
    arr_n = '0' + arr_n

while new_num != n:
    plus = str(int(arr_n[0]) + int(arr_n[1]))
    if len(plus) == 1:
        plus = '0' + plus

    new_num = str(arr_n[1]) + str(plus[-1])
    arr_n = new_num
    cycle += 1
    if int(new_num) == n:
        break

print(cycle)
