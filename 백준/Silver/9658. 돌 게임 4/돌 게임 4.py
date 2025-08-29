import sys

N = int(sys.stdin.readline())
dp = [0] * max(5, N + 1)

dp[1], dp[2], dp[3], dp[4] = "CY", "SK", "CY", "SK"

for j in range(5, N + 1):
    if ((dp[j - 1] == "CY") or (dp[j - 3] == "CY") or (dp[j - 4] == "CY")):
        dp[j] = "SK"
    else:
        dp[j] = "CY"

print(dp[N])