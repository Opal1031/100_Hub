import sys

input = int(input())

for i in range(input):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d: %d + %d =" %(i + 1, a, b), a + b)