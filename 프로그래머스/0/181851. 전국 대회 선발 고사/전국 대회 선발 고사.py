def solution(rank, attendance):
    candidates = []

    for number, (student_rank, can_attend) in enumerate(zip(rank, attendance)):
        if can_attend:
            candidates.append((student_rank, number))

    candidates.sort()

    a = candidates[0][1]
    b = candidates[1][1]
    c = candidates[2][1]

    return 10000 * a + 100 * b + c