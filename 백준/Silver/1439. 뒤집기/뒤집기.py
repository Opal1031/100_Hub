import sys

Num = list(map(int,sys.stdin.readline().strip()))
count = 0

for i in range(len(Num) - 1):
    if Num[i] != Num[i + 1]:
        count += 1

print((count + 1) // 2)