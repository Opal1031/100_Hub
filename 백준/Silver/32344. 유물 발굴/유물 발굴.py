import sys

R, C = map(int, sys.stdin.readline().split())
N = int(sys.stdin.readline())

arr = {}
for _ in range(N):
    a, v, h = map(int, sys.stdin.readline().split())
    if a not in arr:
        arr[a] = [(v, h)]
    else:
        arr[a].append((v, h))

size = []
for k, v in arr.items():
    x_sorted = sorted(v, key=lambda x: x[0])
    x = x_sorted[-1][0] - x_sorted[0][0] + 1

    y_sorted = sorted(v, key=lambda x: x[1])
    y = y_sorted[-1][1] - y_sorted[0][1] + 1

    size.append([k, x * y])

size_sorted = sorted(size, key=lambda x: (-x[1], x[0]))
num, ans = size_sorted[0]
print(num, ans)