N = int(input())

list = []

for i in range(N):
    age, name = input().split()

    list.append([int(age), name])

list.sort(key = lambda x:x[0])

for j in list:
    print(j[0], j[1])