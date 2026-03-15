import sys
input = sys.stdin.readline

N, K = map(int, input().split())

D_list = [[] for _ in range(K)]
T_list_copy = []

for _ in range(N):
    T_list = list(map(int, input().split()))
    T_list_copy.append(T_list)

    for i in range(K):
        T = T_list[i]
        D_list[i].append(T)

M_list = [0 for _ in range(K)]

for i in range(K):
    D = D_list[i]
    M = max(D)
    C = D.count(M)

    if C == 1:
        M_list[i] = M

count = 0

for T_list in T_list_copy:

    for i in range(K):
        T = T_list[i]
        M = M_list[i]

        if T == M:
            count += 1
            break

print(count)