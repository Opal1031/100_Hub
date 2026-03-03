N = int(input())
cnt = 1

while N:
    cnt *= N - 1
    N -= 2

print(cnt % 1000000007)