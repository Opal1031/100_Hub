num = []

for a in range(10):
    new_num = int(input())

    if (new_num % 42) not in num:
        num.append(new_num % 42)

print(len(num))