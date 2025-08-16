import sys

N = int(sys.stdin.readline())
coord = [list(map(int, sys.stdin.readline().split())) for _ in range (N)]

coord.append(coord[0])
sum_x, sum_y = 0, 0

for i in range(N):
    sum_x += coord[i][0] * coord[i + 1][1]
    sum_y += coord[i][1] * coord[i + 1][0]

S = abs(sum_x - sum_y)

print(round((S / 2), 1))