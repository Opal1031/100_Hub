import sys

h1, m1, s1 = map(int, sys.stdin.readline().strip().split(':'))
h2, m2, s2 = map(int, sys.stdin.readline().strip().split(':'))

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

if (t1 > t2):
    print(t2 - t1 + 3600 * 24)

else:
    print(t2 - t1)