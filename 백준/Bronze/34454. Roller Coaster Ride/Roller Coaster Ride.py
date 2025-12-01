import sys

n = int(sys.stdin.readline())
c = int(sys.stdin.readline())
p = int(sys.stdin.readline())

print("yes" if c * p >= n else "no")