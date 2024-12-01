sum = int(input())
num = int(input())

for i in range(num):
    a, b = map(int, input().split())

    sum -= (a * b)

if(sum == 0):
    print("Yes")
else:
    print("No")