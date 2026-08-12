def solution(n):
    prev2, prev1 = 0, 1

    for _ in range(2, n + 1):
        current = (prev2 + prev1) % 1234567
        prev2 = prev1
        prev1 = current

    return prev1