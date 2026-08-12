from collections import deque

def solution(maps):
    rows = len(maps)
    cols = len(maps[0])

    distance = [[-1] * cols for _ in range(rows)]
    distance[0][0] = 1

    queue = deque([(0, 0)])

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    while queue:
        row, col = queue.popleft()

        for i in range(4):
            next_row = row + dr[i]
            next_col = col + dc[i]

            if not (0 <= next_row < rows and 0 <= next_col < cols):
                continue

            if (maps[next_row][next_col] == 0):
                continue

            if (distance[next_row][next_col] != -1):
                continue

            distance[next_row][next_col] = distance[row][col] + 1
            queue.append((next_row, next_col))

    return distance[rows - 1][cols - 1]