import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

dp = [0] * (k + 1)
dp[0] = 1

for coin in coins:
    for s in range(coin, k + 1):
        dp[s] += dp[s - coin]

print(dp[k])