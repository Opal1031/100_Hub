import sys

dp_fib = []
dp_fib.append(1)
dp_fib.append(2)

def fib(n):
    while (dp_fib[-1] < n):
        dp_fib.append(dp_fib[-1] + dp_fib[-2])

while True:
    a, b = map(int, sys.stdin.readline().split())

    if (a == 0 and b == 0):
        break

    else:
        fib(b)
        count = 0

        for i in range(len(dp_fib)):
            if (dp_fib[i] >= a and dp_fib[i] <= b):
                count += 1

        print(count)