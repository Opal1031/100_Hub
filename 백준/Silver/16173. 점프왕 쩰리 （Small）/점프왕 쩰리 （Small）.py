import sys
from collections import deque

def bfs(x, y, visited):
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True

    while dq:
        x, y = dq.popleft()

        if board[x][y] == -1:
            return "HaruHaru"
        
        for j in range(2):
            nx = x + dx[j] * board[x][y]
            ny = y + dy[j] * board[x][y]

            if (0 <= nx < N and 0 <= ny < N and not visited[nx][ny]):
                visited[nx][ny] = True
                dq.append((nx, ny))
    
    return "Hing"

N = int(sys.stdin.readline())
board = []
visited = [[False] * N for _ in range(N)]

for i in range(N):
    row = list(map(int, sys.stdin.readline().split()))
    board.append(row)

dx = [1, 0]
dy = [0, 1]

print(bfs(0, 0, visited))