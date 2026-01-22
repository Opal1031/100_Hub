import sys

x = 1080

for _ in range(10):
    direction = int(sys.stdin.readline())

    if direction == 1:
        x += 90
    elif direction == 2:
        x += 180
    elif direction == 3:
        x -= 90

x //= 90
x %= 4

if x == 0:
    print('N')
elif x == 1:
    print('E')
elif x == 2:
    print('S')
else:
    print('W')