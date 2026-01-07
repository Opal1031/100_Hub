import sys
from collections import deque

def bfs(start, end):
    dq = deque()
    dq.append(start)
    visited = [False] * (N + 1)
    distance = [0] * (N + 1)
    visited[start] = True

    while dq:
        node = dq.popleft()

        if (node == end):
            print(distance[node])
            return
        
        for next_node, dist in graph[node]:
            if not visited[next_node]:
                visited[next_node] = True
                distance[next_node] = distance[node] + dist
                dq.append(next_node)

N, M = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    node1, node2, length = map(int, sys.stdin.readline().split())

    graph[node1].append((node2, length))
    graph[node2].append((node1, length))

for _ in range(M):
    start, end = map(int, sys.stdin.readline().split())
    
    bfs(start, end)