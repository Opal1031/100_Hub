N = int(input())

num = 666
time = 0

while True:
    if "666" in str(num):
        time += 1

    if time == N:
        break

    num += 1

print(num)