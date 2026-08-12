def solution(strArr):
    counts = {}

    for string in strArr:
        length = len(string)
        counts[length] = counts.get(length, 0) + 1

    return max(counts.values())