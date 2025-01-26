N, M = map(int, input().split())

gap = N - M

if gap < 0:
    print(-gap)
else:
    print(gap)