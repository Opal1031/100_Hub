import sys
n = int(sys.stdin.readline())

count1 = 0
count2 = 0

for _ in range(n):
    ch = input()

    if (ch == 'D'):
        count1 += 1
    else:
        count2 += 1

    if (count1 > count2):
        if (count1 == count2 + 2):
            break
        
    else:
        if (count1 + 2 == count2):
            break

print(str(count1) + ":" + str(count2))