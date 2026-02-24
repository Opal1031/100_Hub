import sys

str1 = sys.stdin.readline().strip()
str2 = sys.stdin.readline().strip()

dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]

for i in range(1, len(str1) + 1):
    for j in range(1, len(str2) + 1):
        if (str1[i - 1] == str2[j - 1]):
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])  

print(dp[-1][-1])

LCS = []
i, j = len(str1), len(str2)

while (i > 0 and j > 0):
    if (str1[i - 1] == str2[j - 1]):
        LCS.append(str1[i - 1])
        i -= 1
        j -= 1

    elif (dp[i - 1][j] > dp[i][j - 1]):
        i -= 1

    else:
        j -= 1

if (dp[-1][-1] > 0):
    print(''.join(reversed(LCS)))