import sys

N = int(sys.stdin.readline())
Num_list = list(map(int, sys.stdin.readline().split()))

if (N == 1):
    print(Num_list[0] * Num_list[0])

else:
    print(max(Num_list) * min(Num_list))