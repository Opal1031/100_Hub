import sys

total = 300

for i in range(4):
    time = int(sys.stdin.readline().strip())
    total += time

if (total <= 1800):
    print("Yes")

else:
    print("No")