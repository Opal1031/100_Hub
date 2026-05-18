def solution(numbers, target):
    cnt = 0
    n = len(numbers)

    def dfs(i, s):
        nonlocal cnt

        if (i == n):
            if (s == target):
                cnt += 1

            return
        
        dfs(i+1, s + numbers[i])
        dfs(i+1, s - numbers[i])

    dfs(0, 0)

    return cnt