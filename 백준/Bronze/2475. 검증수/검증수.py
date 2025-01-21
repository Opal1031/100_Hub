Num = map(int, input().split())

result = 0

for i in Num:
    result += i ** 2

print(result % 10)