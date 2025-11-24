N, L = map(int, input().split())

label = 0
count = 0
number = 1

while True:
    if (str(L) not in str(number)):
        label = number
        count += 1

    if (count == N):
        break

    number += 1

print(label)