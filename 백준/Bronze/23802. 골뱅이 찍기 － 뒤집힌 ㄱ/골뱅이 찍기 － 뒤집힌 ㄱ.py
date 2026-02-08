import sys

n = int(sys.stdin.readline())

for _ in range(n):
    print("@@@@@" * n)
    
for _ in range(n * 4):
    print("@" * n)