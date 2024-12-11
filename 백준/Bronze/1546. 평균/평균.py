N = int(input())

subject = list(map(int, input().split()))

M = max(subject)

for b in range(N):
    subject[b] = subject[b] / M * 100

print(sum(subject) / N)