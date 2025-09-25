import sys

B1 = int(sys.stdin.readline().strip(), 2)
B2 = int(sys.stdin.readline().strip(), 2)

print(bin(B1 * B2)[2:])