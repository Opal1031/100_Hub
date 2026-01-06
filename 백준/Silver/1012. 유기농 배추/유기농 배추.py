import sys
from collections import deque

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(x, y):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = 1

    while dq:
        cur_x, cur_y = dq.popleft()

        for i in range(4):
            nx = cur_x + dx[i]
            ny = cur_y + dy[i]

            if ((0 <= nx < N) and (0 <= ny < M)):
                if (board[nx][ny] == 1 and visited[nx][ny] == 0):
                    visited[nx][ny] = 1
                    dq.append((nx, ny))

case = int(sys.stdin.readline())

for _ in range(case):
    M, N, K = map(int, sys.stdin.readline().split())

    board = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        coord_x, coord_y = map(int, sys.stdin.readline().split())
    
        board[coord_y][coord_x] = 1

    cnt = 0

    for p in range(N):
        for q in range(M):
            if (board[p][q] == 1 and visited[p][q] == 0):
                bfs(p, q)
                cnt += 1

    print(cnt)