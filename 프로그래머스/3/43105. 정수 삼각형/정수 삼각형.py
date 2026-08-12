def solution(triangle):
    dp = [row[:] for row in triangle]

    for row in range(1, len(dp)):
        for col in range(len(dp[row])):
            left = dp[row - 1][col - 1] if col > 0 else 0
            right = dp[row - 1][col] if col < len(dp[row - 1]) else 0

            dp[row][col] += max(left, right)

    return max(dp[-1])