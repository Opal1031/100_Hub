import sys

N = int(sys.stdin.readline())
Num_list = [0 for _ in range(N)]

for i in range(N):
    Num_list[i] = int(sys.stdin.readline())

Num_list.sort()

for j in Num_list:
    print(j)