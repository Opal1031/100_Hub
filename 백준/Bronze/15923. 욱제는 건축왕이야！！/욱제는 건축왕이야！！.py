import sys

n = int(sys.stdin.readline())

for i in range(n):
    x, y = map(int, sys.stdin.readline().split())

    if (i == 0):
        x_min, x_max, y_min, y_max = x, x, y, y
        continue

    x_min = min(x_min, x)
    x_max = max(x_max, x)
    y_min = min(y_min, y)
    y_max = max(y_max, y)

width = x_max - x_min
height = y_max - y_min

print((width + height) * 2)