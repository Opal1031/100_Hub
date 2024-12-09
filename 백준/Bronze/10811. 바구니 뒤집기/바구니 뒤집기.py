N, M = map(int, input().split())

bucket = []

for a in range(N):
    bucket.append(a + 1)

for b in range(M):
    i, j = map(int, input().split())

    temp = bucket[i - 1:j]
    temp.reverse()
    bucket[i - 1:j] = temp

for c in range(N):
    print(bucket[c], end = " ")