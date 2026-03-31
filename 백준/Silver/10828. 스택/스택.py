import sys
input = sys.stdin.readline

N = int(input())

stack = []

for _ in range(N):
    cmd = input().strip()

    if cmd.startswith('push'):
        _, num = cmd.split()
        stack.append(int(num))

    elif (cmd == 'pop'):
        print(stack.pop() if stack else -1)

    elif (cmd == 'size'):
        print(len(stack))

    elif (cmd == 'empty'):
        print(0 if stack else 1)

    elif (cmd == 'top'):
        print(stack[-1] if stack else -1)