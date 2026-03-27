import sys
input = sys.stdin.readline

N = int(input())

res = 0

for i in range(N):
    res += 1
    
    if (str(i).find("50") > -1):
        res += 1
        
print(res)