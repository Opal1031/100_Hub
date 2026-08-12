def solution(arr, queries):
    for start, end, step in queries:
        for index in range(start, end + 1):
            if (index % step == 0):
                arr[index] += 1

    return arr