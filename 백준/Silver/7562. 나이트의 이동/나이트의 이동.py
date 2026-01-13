import sys
from collections import deque

dx = [-2, -1, 1, 2, 2, 1, -1, -2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

def bfs(start_x, start_y, end_x, end_y):
    dq = deque()
    dq.append((start_x, start_y))

    visited[start_x][start_y] = True
    board[start_x][start_y] = 0

    while dq:
        x, y = dq.popleft()

        if ((x == end_x) and (y == end_y)):
            print(board[x][y])
            return
        
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]

            if ((0 <= nx < I) and (0 <= ny < I)):
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    board[nx][ny] = board[x][y] + 1
                    dq.append((nx, ny))

T = int(sys.stdin.readline())

for _ in range(T):
    I = int(sys.stdin.readline())

    board = [[0] * I for _ in range(I)]
    visited = [[False] * I for _ in range(I)]

    start_x, start_y = map(int, sys.stdin.readline().split())
    end_x, end_y = map(int, sys.stdin.readline().split())

    bfs(start_x, start_y, end_x, end_y)