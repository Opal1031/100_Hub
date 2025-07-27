import sys

N = int(sys.stdin.readline())
list = []

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())

    money = 0

    if (a == b == c):
        money += 10000 + a * 1000
        list.append(money)

    elif (a == b or a == c or b == c):
        if (a == b or a == c):
            money += 1000 + a * 100
            list.append(money)

        else:
            money += 1000 + b * 100
            list.append(money)
    
    else:
        money += max(a, b, c) * 100
        list.append(money)

print(max(list))