import sys

N = int(sys.stdin.readline())
money = list(map(int, sys.stdin.readline().split()))

y, m = 0, 0

for n in money:
    y += (n // 30 + 1) * 10
    m += (n // 60 + 1) * 15

if (m == y):
    print("Y M", m)

elif (m < y):
    print("M", m)

else:
    print("Y", y)