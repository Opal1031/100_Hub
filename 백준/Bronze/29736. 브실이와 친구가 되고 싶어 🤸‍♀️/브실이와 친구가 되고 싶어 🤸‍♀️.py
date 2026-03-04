a, b = map(int, input().split())
k, x = map(int, input().split())

min = k - x
max = k + x

if max < a:
    print('IMPOSSIBLE')
elif max >= b and a <= min:
    print(b - min + 1)
elif min <= a and max <= b:
    print(max - a + 1)
elif min <= a and max >= b:
    print(b - a + 1)
else:
    print(max - min + 1)