n = int(input())
s = input()

cnte = 0
cnt2 = 0

for i in range(n):
    if s[i] == "2":
        cnt2 += 1
        
    else:
        cnte += 1
        
if cnt2 > cnte:
    print("2")
    
elif cnt2 < cnte:
    print("e")
    
else:
    print("yee")