import sys
input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))
result = 0

nums = [0] * n
nums[0] = a[0]
for i in range(1, n):
    nums[i] = nums[i - 1] + a[i]

nums.sort(reverse = True)

for i in range(k):
    result += nums[i]

print(result)