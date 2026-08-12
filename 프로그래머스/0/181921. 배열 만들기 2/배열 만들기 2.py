def solution(l, r):
    answer = []

    for number in range(l, r + 1):
        is_valid = True

        for digit in str(number):
            if digit not in "05":
                is_valid = False
                break

        if is_valid:
            answer.append(number)

    return answer if answer else [-1]