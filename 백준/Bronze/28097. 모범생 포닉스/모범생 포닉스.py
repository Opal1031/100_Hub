import sys

N = int(sys.stdin.readline())
plan = list(map(int, sys.stdin.readline().split()))
time = sum(plan) + (8 * (N - 1))
 
d, t = time // 24, time % 24
 
print(d, t)