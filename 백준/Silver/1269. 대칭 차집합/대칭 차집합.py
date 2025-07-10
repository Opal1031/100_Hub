import sys

A, B = map(int, sys.stdin.readline().split())

set_A = list(map(int, sys.stdin.readline().split()))
set_B = list(map(int, sys.stdin.readline().split()))

common_set = list(set(set_A) & set(set_B))

print(A + B - (len(common_set) * 2))