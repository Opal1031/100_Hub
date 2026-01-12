import sys

while True:
    try:
        N, M = map(int, sys.stdin.readline().split())
        
    except:
        break
        
    ans = 0
    
    for num in range(N, M + 1):
        cnt = set()
        s_num = str(num)
        
        for char in s_num:
            cnt.add(char)
            
        if (len(s_num) == len(cnt)):
            ans += 1
            
    print(ans)