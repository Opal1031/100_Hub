import sys

l, r, k = map(int, [sys.stdin.readline() for _ in range(3)])

if (k == 2):
    start = max(0, l - 3)
    end = max(0, r - 2)

    print(end - start)

elif (k == 3):
    start = max(0, (l - 1) // 3 - 1)
    end = max(0, r // 3 - 1)

    print(end - start)

elif (k == 4):
    start = max(0, (l - 1) // 2  - 4)
    end = max(0, r // 2 - 4)

    if ((l - 1) >= 12):
        start -= 1

    if (r >= 12):
        end -= 1

    print(end - start)

else:
    start = max(0, (l - 1) // 5 - 2)
    end = max(0, r // 5 - 2)

    print(end - start)