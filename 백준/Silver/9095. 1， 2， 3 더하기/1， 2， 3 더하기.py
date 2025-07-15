import sys

N = int(sys.stdin.readline())

dp = [0] * 10
dp[0], dp[1], dp[2] = 1, 2, 4

for i in range(3, 10):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

for j in range(N):
    num = int(sys.stdin.readline())

    print(dp[num - 1])