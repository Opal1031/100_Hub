def solution(sequence, k):
    answer = []

    left = right = total = 0
    min_len = 1000000

    while (right < len(sequence)):
        total += sequence[right]

        while (total > k and left <= right):
            total -= sequence[left]
            left += 1

        if (total == k):
            if (right - left < min_len):
                min_len = right - left
                answer = [left, right]

        right += 1
        
    return answer