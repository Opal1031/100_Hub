import sys

S = sys.stdin.readline().strip()

for idx in range(len(S)):
    if S[idx:] == S[idx:][::-1]:
        print(len(S) + idx)
        break