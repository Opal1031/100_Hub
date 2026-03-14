import sys

N, K = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))

def bubble_sort(lst, K):
    cnt = 0

    for i in range(len(lst), 0, -1):
        for j in range(i - 1):
            if lst[j] > lst[j + 1]:
                cnt += 1
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

                if cnt == K:
                    print(*lst)
                    return

    print(-1)

bubble_sort(A, K)