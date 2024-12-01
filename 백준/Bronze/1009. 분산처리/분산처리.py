a = []
b = []

t = int(input())

for i in range(t):
    num2, num3 = input().split()
    a.append(int(num2))
    b.append(int(num3))

for x in range(t):
    base = a[x] % 10

    if base == 0:
        print(10)

    elif base in [1, 5, 6]:
        print(base)

    elif base in [4, 9]:
        if b[x] % 2 == 0:
            print(base ** 2 % 10)
        else:
            print(base)

    else:
        if b[x] % 4 == 0:
            print(base ** 4 % 10)
        else:
            print(base ** (b[x] % 4) % 10)