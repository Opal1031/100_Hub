import sys
input = sys.stdin.readline

N, M, K = map(int, input().split())
arr = [int(input()) for _ in range(N)]

size = 1

while (size < N):
    size *= 2

tree = [0] * (2 * size)

# 트리 초기화
for i in range(N):
    tree[size + i] = arr[i]

for i in range(size - 1, 0, -1):
    tree[i] = tree[2 * i] + tree[2 * i + 1]

def update(idx, value):
    idx += size

    tree[idx] = value

    while (idx > 1):
        idx //= 2
        tree[idx] = tree[2 * idx] + tree[2 * idx + 1]

def query(left, right):
    left += size
    right += size
    res = 0

    while (left <= right):
        if (left % 2 == 1):
            res += tree[left]
            left += 1

        if (right % 2 == 0):
            res += tree[right]
            right -= 1

        left //= 2
        right //= 2
    return res

for _ in range(M + K):
    a, b, c = map(int, input().split())

    if (a == 1):
        update(b - 1, c)

    elif (a == 2):
        print(query(b - 1, c - 1))