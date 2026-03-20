import sys
from collections import deque

input = sys.stdin.readline

N, M, V = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N + 1):
    graph[i].sort()

def dfs(v, visited):
    visited[v] = True
    print(v, end = " ")

    for p in graph[v]:
        if not visited[p]:
            dfs(p, visited)

def bfs(v, visited):
    queue = deque([v])
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end = " ")

        for q in graph[v]:
            if not visited[q]:
                queue.append(q)
                visited[q] = True

visited = [False] * (N + 1)
dfs(V, visited)
print()
visited = [False] * (N + 1)
bfs(V, visited)