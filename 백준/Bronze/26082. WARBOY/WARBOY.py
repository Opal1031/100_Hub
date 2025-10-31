import sys

A, B, C = map(int, sys.stdin.readline().split())

competition = B / A

print(int(competition * 3 * C))