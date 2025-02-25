N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())

score = 0
sum_score = 0

for i in range(len(size)):
    if (size[i] % T) == 0:
        score = size[i] // T
    else:
        score = size[i] // T + 1
    sum_score += score


print(sum_score)
print(N // P, N % P)