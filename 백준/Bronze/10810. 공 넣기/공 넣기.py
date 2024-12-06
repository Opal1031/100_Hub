N, M = map(int, input().split())

bucket = []

for a in range(N):
    bucket.append(0)

for b in range(M):
    i, j, k = map(int, input().split())
    
    for c in range(i, j + 1):
        bucket[c - 1] = k
        
for d in range(N):
    print(bucket[d], end = " ")