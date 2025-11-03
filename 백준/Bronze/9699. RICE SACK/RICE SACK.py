import sys

for i in range(int(sys.stdin.readline())):
    tmp = max(map(int, sys.stdin.readline().split()))
    
    print(f"Case #{i + 1}: {tmp}")