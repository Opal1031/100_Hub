import sys
from collections import deque

def DSLR_calc(prev, result):
    dq = deque()
    visited = [False] * 10000

    dq.append((prev, ""))
    visited[prev] = True

    while dq:
        curr, op = dq.popleft()

        if curr == result:
            return op

        D = (curr * 2) % 10000
        if not visited[D]:
            visited[D] = True
            dq.append((D, op + "D"))

        S = (curr - 1) % 10000
        if not visited[S]:
            visited[S] = True
            dq.append((S, op + "S"))

        L = (curr % 1000) * 10 + (curr // 1000)
        if not visited[L]:
            visited[L] = True
            dq.append((L, op + "L"))

        R = (curr % 10) * 1000 + (curr // 10)
        if not visited[R]:
            visited[R] = True
            dq.append((R, op + "R"))


T = int(sys.stdin.readline())

for _ in range(T):
    prev, result = map(int, sys.stdin.readline().split())

    print(DSLR_calc(prev, result))    