import sys

for i in range(2):
    T, F, S, P, C = map(int, sys.stdin.readline().split())

    print(6 * T + 3 * F + 2 * S + P + 2 * C)