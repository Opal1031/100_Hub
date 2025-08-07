import sys

N = int(sys.stdin.readline())
Num = 1

for i in range(1, N + 1):
    Num *= i

Num_list = list(str(Num))

for j in range(len(Num_list) -1, -1, -1):
    if (Num_list[j] == '0'):
        continue

    else:
        print(Num_list[j])
        break