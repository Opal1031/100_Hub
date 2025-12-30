import sys
from collections import deque

def bfs(start, graph):
    dq = deque()
    dq.append(start - 1)
    visited[start - 1] = True
    cnt = 0

    while dq:
        current = dq.popleft()

        for edge in graph:
            a, b = edge[0] - 1, edge[1] - 1
            
            if a == current and not visited[b]:
                dq.append(b)
                visited[b] = True
                cnt += 1

    return cnt

Com = int(sys.stdin.readline())
connect = int(sys.stdin.readline())

graph = []
visited = [False] * Com

for i in range(connect):
    a, b = map(int, sys.stdin.readline().split())
    graph.append((a, b))
    graph.append((b, a))

print(bfs(1, graph))