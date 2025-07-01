N, M = map(int, input().split())
mat = [list(map(int, input().strip())) for _ in range(N)]

max_size = min(N, M)

for size in range(max_size, 0, -1):
    for y in range(N - size + 1):
        for x in range(M - size + 1):
            a = mat[y][x]
            b = mat[y][x + size - 1]
            c = mat[y + size - 1][x]
            d = mat[y + size - 1][x + size - 1]
            
            if a == b == c == d:
                print(size * size)
                exit()