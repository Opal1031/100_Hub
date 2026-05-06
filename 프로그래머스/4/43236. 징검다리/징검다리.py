def solution(distance, rocks, n):
    answer = 0

    rocks.sort()
    
    left, right = 1, distance
    
    while (left <= right):
        mid = (left + right) // 2
        
        count = 0
        prev = 0
        
        for rock in rocks:
            if (rock - prev < mid):
                count += 1

            else:
                prev = rock
        
        if (distance - prev < mid):
            count += 1
        
        if (count <= n):
            answer = mid
            left = mid + 1

        else:
            right = mid - 1
    
    return answer