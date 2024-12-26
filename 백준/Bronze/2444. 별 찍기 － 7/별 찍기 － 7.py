# BAEKJOON

N = int(input())
star = 1

for i in range(N):
    print(" " * (N - 1 - i) + "*" * star)
    star += 2

for j in range(N - 1):
    print(" " * (j + 1) + "*" * (star - 4))
    star -= 2