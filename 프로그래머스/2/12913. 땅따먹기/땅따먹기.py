def solution(land):
    dp = [row[:] for row in land]

    for row in range(1, len(dp)):
        for col in range(4):
            previous = [dp[row - 1][i] for i in range(4) if i != col]
            dp[row][col] += max(previous)

    return max(dp[-1])