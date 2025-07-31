import sys

N = int(sys.stdin.readline())
Num = 1

for i in range(1, N + 1):
    if (N == 0):
        Num = 1
        break

    Num *= i

print(Num)