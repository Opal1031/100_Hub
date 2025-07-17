import sys

fib_num = [0] * 28
fib_num[0], fib_num[1] = 1, 1

for i in range(2, 28):
    fib_num[i] = fib_num[i - 1] + fib_num[i - 2]

D, K = map(int, sys.stdin.readline().split())

Flag = False
Count_A, Count_B = 0, 0

for A in range(1, K + 1):
    for B in range(1, K + 1):
        Cake = fib_num[D - 3] * A + fib_num[D - 2] * B

        if Cake == K:
            Flag = True
            Count_A, Count_B = A, B
            break

    if Flag:
        break

print(Count_A)
print(Count_B)