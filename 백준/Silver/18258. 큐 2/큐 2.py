import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

dq = deque()

for _ in range(N):
    cmd = input().strip()

    if cmd.startswith('push'):
        _, num = cmd.split()
        dq.append(int(num))

    elif (cmd == 'pop'):
        print(dq.popleft() if dq else -1)

    elif (cmd == 'size'):
        print(len(dq))

    elif (cmd == 'empty'):
        print(0 if dq else 1)

    elif (cmd == 'front'):
        print(dq[0] if dq else -1)

    elif (cmd == 'back'):
        print(dq[-1] if dq else -1)