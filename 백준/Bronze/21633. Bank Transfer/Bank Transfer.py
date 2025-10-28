import sys

redgotts = int(sys.stdin.readline().strip())
bluegotts = float((redgotts * 0.01) + 25.00)

if (bluegotts <= 100):
    print("100")
elif (bluegotts >= 2000):
    print("2000")
else:
    print("{:.2f}".format(bluegotts))