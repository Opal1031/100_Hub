for _ in range(int(input())):
    s = input()
    
    hg = s[0::2]
    tw = s[1::2]
    
    if len(s) % 2 == 1:
        hg += s[1::2]
        tw += s[0::2]
        
    print(hg)
    print(tw)