N = int(input())

list = []

for i in range(N):
    word = input()
    
    if word not in list:
        list.append(word)

list.sort()
list.sort(key = len)

for k in list:
    print(k)