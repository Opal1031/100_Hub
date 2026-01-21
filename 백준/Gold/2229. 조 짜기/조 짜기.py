import sys

N = int(sys.stdin.readline().strip())
age = list(map(int, sys.stdin.readline().split()))

dp = [0 for _ in range(N + 1)]

for i in range(N + 1):
    for k in range(i - 1, -1, -1): 
        score = max(age[k:i]) - min(age[k:i])
        dp[i] = max(dp[k] + score, dp[i])
        
print(dp[-1])