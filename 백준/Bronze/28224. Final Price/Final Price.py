import sys

n = int(sys.stdin.readline())
ans = 0

for _ in range(n):
    a = int(sys.stdin.readline())
    ans += a
    
print(ans)