import sys

n = int(sys.stdin.readline())
towers = list(map(int, sys.stdin.readline().split()))

count = 1

for i in range(n - 1):
    if (towers[i] <=  towers[i + 1]):
        count += 1
        
print(count)