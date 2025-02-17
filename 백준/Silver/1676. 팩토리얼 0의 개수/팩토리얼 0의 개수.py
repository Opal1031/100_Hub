N = int(input())

fac_Num = 1
count = 0

list = []

for i in range(N):
    fac_Num *= (i + 1)

for j in str(fac_Num):
    list.append(j)

list.reverse()

for k in range(len(list)):
    if list[k] == "0":
        count += 1

    else:
        break

print(count)