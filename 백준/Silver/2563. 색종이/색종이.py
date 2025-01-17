base = [[0 for i in range(100)] for i in range(100)]

N = int(input())

S = 0

for j in range(N):
    paper = list(map(int, input().split()))

    for row in range(paper[1], paper[1] + 10):
        for col in range(paper[0], paper[0] + 10):
            base[row][col] = 1

for k in base:
    S += sum(k)

print(S)