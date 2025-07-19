import sys

Num = int(sys.stdin.readline())
dp = list(range(Num + 1))

for i in range(2, Num + 1):
    for j in range(1, i + 1):
        square = j * j

        if square > i:
            break

        dp[i] = min(dp[i], dp[i - square] + 1)

print(dp[Num])