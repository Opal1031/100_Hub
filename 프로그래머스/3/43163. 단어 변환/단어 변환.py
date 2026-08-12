from collections import deque

def solution(begin, target, words):
    if target not in words:
        return 0

    queue = deque([(begin, 0)])
    visited = set([begin])

    while queue:
        current, count = queue.popleft()

        if (current == target):
            return count

        for word in words:
            difference = 0

            for a, b in zip(current, word):
                if (a != b):
                    difference += 1

            if (difference == 1 and word not in visited):
                visited.add(word)
                queue.append((word, count + 1))

    return 0