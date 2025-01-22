A = int(input())
B = int(input())
C = int(input())

Num = A * B * C
Num_list = list(map(int, str(Num)))

for i in range(10):
    print(Num_list.count(i))