import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m, r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
cnt = 0

for i in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


for i in range(1, n+1):
    graph[i].sort(reverse=True)


def dfs(start):
    global cnt
    cnt += 1
    visited[start] = cnt

    for i in graph[start]:
        if not visited[i]:
            dfs(i)


dfs(r)

print(*visited[1:], sep = '\n')