import sys
X = int(sys.stdin.readline().strip())
N = int(sys.stdin.readline().strip())
V = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    V += a * b
if X == V: print("Yes")
else: print("No")