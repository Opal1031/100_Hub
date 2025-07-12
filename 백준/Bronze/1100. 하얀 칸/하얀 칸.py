import sys

board = [[0 for _ in range(8)] for _ in range(8)]
count = 0

for i in range(8):
    chess = sys.stdin.readline().strip()
    board[i] = list(chess)

for p in range(8):
    for q in range(8):
        if board[p][q] == "F":
            if ((p + q) % 2 == 0):
                count += 1

print(count)