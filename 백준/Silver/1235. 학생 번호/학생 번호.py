N = int(input())
mat = [input().strip() for _ in range(N)]

length = len(mat[0])

for i in range(1, length + 1):
    check = set()

    for j in mat:
        sub_num = j[-i:]
        check.add(sub_num)

    if len(check) == N:
        print(i)
        break