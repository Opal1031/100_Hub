import sys

N = int(sys.stdin.readline())
dp = [False] * (N + 5)

dp[1], dp[2], dp[3], dp[4] = True, False, True, True

for i in range(5, N + 1):
    if (not dp[i - 1] or not dp[i - 3] or not dp[i - 4]):
        dp[i] = True

    else:
        dp[i] = False

print("SK" if dp[N] else "CY")