N, M = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
check = set(A) - set(B)

print(len(check))

if len(check) != 0:
    print(*sorted(check))