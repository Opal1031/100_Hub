while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    else:
        list = [a, b, c]
        list.sort()

        if list[0] ** 2 + list[1] ** 2 == list[2] ** 2:
            print("right")
        
        else:
            print("wrong")