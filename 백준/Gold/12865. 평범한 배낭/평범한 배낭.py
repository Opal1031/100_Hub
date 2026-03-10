import sys

N, K = map(int, sys.stdin.readline().split())
DP = [0] * (K + 1)

for _ in range(N):
    W, V = map(int, sys.stdin.readline().split())
    
    for j in range(K, W - 1, -1):
        DP[j] = max(DP[j], DP[j - W] + V)

print(DP[K])