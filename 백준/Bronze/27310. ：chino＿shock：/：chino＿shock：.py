import sys

str = sys.stdin.readline().strip()

len = len(str)
bar = 0

for _ in range(0, len):
    if (str[_] == "_"):
        bar += 1

print(len + 2 + bar * 5)