import sys

a,b = map(int, sys.stdin.readline().split())

if ((a - a * 0.01 * b) >=100):
    print(0)
    
else:
    print(1)