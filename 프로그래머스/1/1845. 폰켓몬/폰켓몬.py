def solution(nums):
    kinds = set(nums)
    limit = len(nums) // 2

    return min(len(kinds), limit)