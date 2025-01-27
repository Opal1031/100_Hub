X, Y, W, H = map(int, input().split())

list = [X, Y, W - X, H - Y]

list.sort()

print(list[0])