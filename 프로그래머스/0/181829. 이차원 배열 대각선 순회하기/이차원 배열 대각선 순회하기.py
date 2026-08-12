def solution(board, k):
    answer = 0

    for row, values in enumerate(board):
        for col, value in enumerate(values):
            if (row + col <= k):
                answer += value

    return answer