a, b, c = map(int, input().split())

if(a == b == c):
    print(10000 + a * 1000)
elif(a == b or b == c or c == a):
    if(a == b or b == c):
        print(1000 + b * 100)
    else:
        print(1000 + c * 100)
else:
    print(100 * max(a, b, c))