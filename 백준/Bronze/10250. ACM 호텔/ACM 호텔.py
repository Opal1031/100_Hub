T = int(input())

for i in range(T):
    H, W, N = map(int, input().split())

    if N % H == 0:
        YY = H
        XX = N // H
    else:
        YY = N % H
        XX = N // H + 1

    print(YY * 100 + XX)