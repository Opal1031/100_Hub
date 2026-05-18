def solution(s):
    counts = {}

    for ch in s.lower():
        counts[ch] = counts.get(ch, 0) + 1
        
    return counts.get('p', 0) == counts.get('y', 0)