import sys

N, K = map(int, sys.stdin.readline().split())
Ans = [[] for _ in range(N)]

for i in range(N):
    for j in range(i + 1):
        if (i == 0) or (j == 0) or (j == i):
            Ans[i].append(1)
        
        else:
            Ans[i].append(Ans[i - 1][j - 1] + Ans[i - 1][j])

print(Ans[N - 1][K - 1])