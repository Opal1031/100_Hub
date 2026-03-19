import sys
input = sys.stdin.readline

N = int(input())

for i in range(N):
    a, b = map(str, input().split())

    if (b == "2026"):
        print(a)

        break