n = int(input())
S = list(input())

for i in range(n):
    if S[i] == "I":
        S[i] = "i"
    else:
        S[i] = "L"

for j in range(n):
    print(S[j], end = "")