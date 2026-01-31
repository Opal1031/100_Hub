import sys

def diagonal_intersections(n):
    if (n < 4):
        return 0
    
    return n * (n - 1) * (n - 2) * (n - 3) // 24

N = int(sys.stdin.readline())

print(diagonal_intersections(N))