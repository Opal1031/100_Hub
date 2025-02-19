while True:
    N = int(input())

    if N == 0:
        break

    else:
        Sum = 0

        for i in range(N):
            Sum += i + 1

        print(Sum)