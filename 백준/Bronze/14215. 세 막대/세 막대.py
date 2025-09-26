import sys

arr = list(map(int, sys.stdin.readline().split()))

arr.sort()
a, b, c = arr

if (a + b <= c):
    c = a + b - 1

print(a + b + c)