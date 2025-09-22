import sys

x = []
n = int(sys.stdin.readline().strip())

for i in range(n):
    x.append(list(map(int,sys.stdin.readline().strip().split())))

print("Gnomes:")

for i in x:
    if (i == sorted(i) or i == sorted(i, reverse=True)):
        print("Ordered")

    else:
        print("Unordered")