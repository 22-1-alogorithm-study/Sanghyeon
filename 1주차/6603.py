def dfs(start, depth):
    if depth == 6:
        for i in range(6):
            print(combi[i], end=' ')
        print()
        return
    for i in range(start, len(s)):
        combi[depth] = s[i]
        dfs(i + 1, depth + 1)


combi = [0 for i in range(13)]


while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    if k == 0:
        break
    dfs(0, 0)
    print()
