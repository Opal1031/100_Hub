import sys

N, M = map(int, sys.stdin.readline().split())

if (M == 1 or M == 2):
    print("NEWBIE!")

elif (M <= N):
    print("OLDBIE!")

else:
    print("TLE!")