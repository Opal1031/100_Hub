def solution(arr, delete_list):
    deleted = set(delete_list)

    return [number for number in arr if number not in deleted]