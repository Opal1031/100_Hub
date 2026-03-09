import sys

n = int(sys.stdin.readline())
numbers = sorted(list(map(int, sys.stdin.readline().split())))
x = int(sys.stdin.readline())

cnt = 0
left, right = 0, n - 1

while (left < right):
    tmp = numbers[left] + numbers[right]

    if tmp == x:
        cnt += 1
        left += 1

    elif tmp < x:
        left += 1
        
    else:
        right -= 1

print(cnt)