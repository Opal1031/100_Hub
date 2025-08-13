import sys
import math

Xa, Ya, Xb, Yb, Xc, Yc = map(int, sys.stdin.readline().split())

if ((Xa * (Yb - Yc) + Xb * (Yc - Ya) + Xc * (Ya - Yb)) == 0):
    print(-1)
    sys.exit()

def dist(x1, y1, x2, y2):
    return math.hypot(x1 - x2, y1 - y2)

a = dist(Xa, Ya, Xb, Yb)
b = dist(Xb, Yb, Xc, Yc)
c = dist(Xc, Yc, Xa, Ya)

circum = [2 * (a + b), 2 * (b + c), 2 * (c + a)]

circum.sort()

print((circum[-1] - circum[0]))