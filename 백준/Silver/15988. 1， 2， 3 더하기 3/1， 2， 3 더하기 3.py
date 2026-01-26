import sys

MOD = 1000000009
MAX_N = 1000000

dp = [0] * (MAX_N + 1)
dp[0] = 1

for i in range(1, MAX_N + 1):
    if (i - 1 >= 0):
        dp[i] = (dp[i] + dp[i-1]) % MOD
    if (i - 2 >= 0):
        dp[i] = (dp[i] + dp[i-2]) % MOD
    if (i - 3 >= 0):
        dp[i] = (dp[i] + dp[i-3]) % MOD

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())

    print(dp[n])