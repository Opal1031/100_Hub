import sys

N = int(sys.stdin.readline())
lst = list(map(str, sys.stdin.readline().split()))

for i in range(N):
    print(lst[i] + "DORO", end = " ")