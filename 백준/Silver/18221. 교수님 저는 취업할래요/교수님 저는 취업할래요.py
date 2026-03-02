import sys
input = sys.stdin.readline

n = int(input())
arr = []
pro = None
seong_gyu = None

for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)
    
    if 5 in nums:
        pro = (nums.index(5), i)
        
    if 2 in nums:
        seong_gyu = (nums.index(2), i)

x1, x2 = min(pro[0], seong_gyu[0]), max(pro[0], seong_gyu[0])
y1, y2 = min(pro[1], seong_gyu[1]), max(pro[1], seong_gyu[1])

cnt = 0

for y in range(y1, y2+1):
    cnt += arr[y][x1: x2+1].count(1)

if cnt >= 3 and (x1 - x2) ** 2 + (y1 - y2) ** 2 >= 25:
    print(1)
else:
    print(0)