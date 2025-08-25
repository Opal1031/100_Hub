import sys

N = int(sys.stdin.readline())

Num = 1
cnt = 1

while (N > Num):
    Num += 6 * cnt
    cnt += 1

print(cnt)