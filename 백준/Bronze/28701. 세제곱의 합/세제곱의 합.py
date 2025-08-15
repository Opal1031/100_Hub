import sys

N = int(sys.stdin.readline())

single = 0
triple = 0

for i in range(1, N + 1):
    single += i
    triple += i ** 3

print(single)
print(single ** 2)
print(triple)