import sys

T = int(sys.stdin.readline())

dp = [0] * 40
dp[0], dp[1] = 1, 1

for i in range(T):
    N = int(sys.stdin.readline())

    if (N == 0):
        print(1, 0)
        continue

    elif (N == 1):
        print(0, 1)
        continue

    else:
        for j in range(2, N):
            dp[j] = dp[j - 1] + dp[j - 2]

        print(dp[N - 2], dp[N - 1])