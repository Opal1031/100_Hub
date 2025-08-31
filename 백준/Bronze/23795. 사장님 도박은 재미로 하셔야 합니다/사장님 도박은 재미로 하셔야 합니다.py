import sys

money = 0
Flag = True

while Flag:
    N = int(sys.stdin.readline())

    if (N == -1):
        Flag = False
        break

    money += N

print(money)