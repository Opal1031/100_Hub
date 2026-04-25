def solution(strlist):
    answer = [0] * 52
    
    for c in my_string:
        if ("A" <= c <= "Z"):
            answer[ord(c) - 65] += 1
            
        elif ("a" <= c <= "z"):
            answer[ord(c) - 71] += 1
            
    return answer