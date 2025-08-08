import sys

N = int(sys.stdin.readline())

list = [int(x) for x in sys.stdin.readline().split()]
prefix_sum = [0] * (N + 1)

for i in range(N):
    prefix_sum[i + 1] = prefix_sum[i] + list[i]    

M = int(sys.stdin.readline())

for j in range(M):
    start, end = map(int, sys.stdin.readline().split())

    total = prefix_sum[end] - prefix_sum[start - 1]    

    print(total)