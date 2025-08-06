import sys

N = int(sys.stdin.readline())

line = sorted([int(sys.stdin.readline()) for _ in range(N)], reverse = True)
Ans = -1

for i in range(N - 2):
    if (line[i] < line[i + 1] + line[i + 2]):
        Ans = line[i] + line[i + 1] + line[i + 2]

        break

print(Ans)