import sys

K, N, M = map(int, sys.stdin.readline().split())

money = K * N - M

if (money <= 0):
    print("0")

else:
    print(money)