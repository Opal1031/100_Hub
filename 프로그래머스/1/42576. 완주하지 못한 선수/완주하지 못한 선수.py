def solution(participant, completion):
    counts = {}

    for name in participant:
        counts[name] = counts.get(name, 0) + 1

    for name in completion:
        counts[name] -= 1

    for name, count in counts.items():
        if (count > 0):
            return name