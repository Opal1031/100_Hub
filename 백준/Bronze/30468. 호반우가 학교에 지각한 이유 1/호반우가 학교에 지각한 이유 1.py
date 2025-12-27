import sys

STR, DEX, INT, LUK, N = map(int, sys.stdin.readline().split())
avg = (STR + DEX + INT + LUK) / 4
 
if (N - avg > 0):
    print(int((N - avg) * 4))
else:
    print(0)