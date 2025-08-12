import sys

N = int(sys.stdin.readline())

for _ in range(N):
    PS = list(map(str, sys.stdin.readline().strip()))
    count = 0
    vps = True

    for ps in PS:
        if ps == '(':
            count += 1

        elif ps == ')':
            count -= 1

        if (count < 0):
            vps = False
            break

    if (vps and (count == 0)):
        print("YES")

    else:
        print("NO")