import sys

A, B = map(int, sys.stdin.readline().split())

if (A >= B / 2):
    print("E")

else:
    print("H")