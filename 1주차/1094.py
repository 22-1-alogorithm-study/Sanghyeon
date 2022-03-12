x = int(input())


def function():
    first_stick = 64  # 초반 막대 길이.
    stick = []  # 붙여질 막대 배열.
    result = int(sum(stick))  # 막대를 붙인 길이.
    temp = x

    while result != x and temp != 0:
        if first_stick > temp:
            first_stick = first_stick // 2
        else:
            stick.append(first_stick)
            temp = temp - first_stick

    return len(stick)


print(function())
