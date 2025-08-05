import sys

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

N = int(sys.stdin.readline())
Tag = int(sys.stdin.readline())

mat = [[0] * N for _ in range(N)]

Num = N * N
i, j = 0, 0
dir = 0
Tag_dx, Tag_dy = 0, 0

while (Num > 0):
    mat[i][j] = Num
    
    if (Num == Tag):
        Tag_dx, Tag_dy = i + 1, j + 1
    
    Num -= 1
    
    if (Num > 0):
        if (((i + dx[dir]) < 0) or ((i + dx[dir]) >= N) or
            ((j + dy[dir]) < 0) or ((j + dy[dir]) >= N) or
            (mat[i + dx[dir]][j + dy[dir]] != 0)):
            dir = (dir + 1) % 4
        
        i += dx[dir]
        j += dy[dir]

for i in mat:
    print(*i)

print(Tag_dx, Tag_dy)