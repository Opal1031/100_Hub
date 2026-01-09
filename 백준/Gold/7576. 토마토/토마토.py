import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs():
    dq = deque()
    max_day = 0

    for i in range(N):
        for j in range(M):
            if (box[i][j] == 1) and (not visited[i][j]):
                dq.append((i, j, 0))
                visited[i][j] = True

    while dq:
        x, y, day = dq.popleft()
        max_day = max(max_day, day)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if (0 <= nx < N) and (0 <= ny < M):
                if (box[nx][ny] == 0) and (not visited[nx][ny]):
                    box[nx][ny] = 1
                    dq.append((nx, ny, day + 1))
                    visited[nx][ny] = True

                if (box[nx][ny] == -1) and (not visited[nx][ny]):
                    visited[nx][ny] = True

    for p in range(N):
        for q in range(M):
            if (box[p][q] == 0):
                print(-1)
                return
            
    print(max_day)

M, N = map(int, sys.stdin.readline().split())

box = []
visited = [[False] * M for _ in range(N)]

for _ in range(N):
    box.append(list(map(int, sys.stdin.readline().split())))

bfs()