import sys
input = sys.stdin.readline

def backtracking(start, path):
    if (len(path) == L):
        vowel_count = 0

        for char in path:
            if char in "aeiou":
                vowel_count += 1

        consonant_count = L - vowel_count

        if (vowel_count >= 1 and consonant_count >= 2):
            print("".join(path))
        
        return
    
    for i in range(start, C):
        path.append(chars[i])
        backtracking(i + 1, path)
        path.pop()

L, C = map(int, input().split())

chars = sorted(input().split())

backtracking(0, [])