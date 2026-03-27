import sys
input = sys.stdin.readline

N = int(input())
Num = 1

if (N == 0):
    print(1)

else:
    for i in range(1, N + 1):
        Num *= i

    print(Num)