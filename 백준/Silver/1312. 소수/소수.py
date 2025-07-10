import sys

A, B, N = map(int, sys.stdin.readline().split())

for i in range(N):
    A = (A % B) * 10

dec = A // B

print(dec)