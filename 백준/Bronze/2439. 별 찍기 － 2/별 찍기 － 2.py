import sys

star = "*"
num = int(sys.stdin.readline())

for i in range(num):
    print(" " * (num - i - 1) + star * (i + 1))