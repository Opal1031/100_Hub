import sys

A, B = map(int, sys.stdin.readline().split())

def check_prime(num):
    if num == 1:
        return False
    
    else:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
            
        return True
    
for j in range(A, B + 1):
    if check_prime(j):
        print(j)