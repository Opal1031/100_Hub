m = int(input())
n = int(input())
li = []

for i in range(m, n + 1):
    e = 0
    
    if (i > 1):
        for j in range(2, i):
            if (i % j == 0):
                e += 1
                break
                
        if (e == 0):
            li.append(i)

if (len(li) < 1):
    print(-1)
    
else:
    print(sum(li))
    print(min(li))