import sys

N, M = map(int, sys.stdin.readline().split())

for _ in range(N):
    line = sys.stdin.readline().rstrip()
    print(line[::-1])