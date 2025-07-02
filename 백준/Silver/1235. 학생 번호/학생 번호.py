N = int(input())
mat = [input().strip() for _ in range(N)]

length = len(mat[0])

for i in range(1, length + 1):
    check = set()

    for num in mat:
        suffix = num[-i:]
        check.add(suffix)

    if len(check) == N:
        print(i)
        break