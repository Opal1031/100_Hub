def solution(numbers):
    present = {i: 0 for i in range(10)}

    for n in numbers:
        present[n] = 1
        
    return sum(k for k, v in present.items() if v == 0)