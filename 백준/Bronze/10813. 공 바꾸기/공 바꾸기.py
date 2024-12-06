N, M = map(int, input().split())

bucket = []

for a in range(N):
    bucket.append(a + 1)

for b in range(M):
    i, j = map(int, input().split())
    
    bucket[i - 1], bucket[j - 1] = bucket[j - 1], bucket[i -1]

for d in range(N):
    print(bucket[d], end = " ")