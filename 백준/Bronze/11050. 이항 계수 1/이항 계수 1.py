import sys

def factorial(n):
    if (n == 0 or n == 1):
        return 1
    
    else:
        return (n * factorial(n - 1))
    

n, k = map(int, sys.stdin.readline().split())
result = factorial(n) // (factorial(k) * factorial(n - k))

print(result)