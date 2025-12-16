import sys

N, I = map(int, sys.stdin.readline().split())
 
lst = []
 
for _ in range(N):
    handle = sys.stdin.readline().strip()
    lst.append(handle)

lst.sort()
 
print(lst[I - 1])