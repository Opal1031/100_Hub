import sys

N = int(sys.stdin.readline())

sum1 = N * (N + 1) // 2
sum2 = (N + 1) * (N + 2) // 2 - 1

res1 = sum1 % 2
res2 = sum2 % 2

if (res1 == res2 == 0):
    print(2)

elif (res1 == res2 == 1):
    print(1)

else:
    print(0)