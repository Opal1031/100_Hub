cnt = 0

while True:
    cnt += 1
    a,b,c = map(int, input().split())
    if a == 0 and b == 0 and c == 0:
        break
        
    if cnt > 1:
        print()
        
    if c == -1:
        print(f"Triangle #{cnt}")
        print("c = %.3f" % ((a**2+b**2)**0.5))
        
    elif max(a, b) >= c:
        print(f"Triangle #{cnt}")
        print('Impossible.')
        
    elif a == -1:
        print(f"Triangle #{cnt}")
        print("a = %.3f" % ((c**2-b**2)**0.5))
        
    elif b == -1:
        print(f"Triangle #{cnt}")
        print("b = %.3f" % ((c**2-a**2)**0.5))