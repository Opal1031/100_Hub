Num, Compare = map(int, input().split())

list = list(map(int, input().split()))

for i in range(Num):
    if(list[i] < Compare):
        print(list[i])

    else:
        continue