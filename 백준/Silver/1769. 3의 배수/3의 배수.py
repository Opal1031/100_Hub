import sys

X = sys.stdin.readline().strip()
count = 0

while len(X) > 1:
    Sum = sum(int(digit) for digit in X)
    X = str(Sum)
    count += 1

if (int(X) % 3 == 0):
    result = "YES"

else:
    result = "NO"

print(count)
print(result)