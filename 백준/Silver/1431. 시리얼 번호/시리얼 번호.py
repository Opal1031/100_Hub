import sys

N = int(sys.stdin.readline())
serial = [[] for _ in range(N)]

for i in range(N):
    Num = sys.stdin.readline()
    Sum = 0

    for j in range(len(Num.strip())):
        if Num[j].isdigit():
            Sum += int(Num[j])

    serial[i].append(len(Num.strip()))
    serial[i].append(Sum)
    serial[i].append(Num.strip())

serial.sort(key = lambda x : (x[0], x[1], x[2]))

print("\n".join(j[2] for j in serial))