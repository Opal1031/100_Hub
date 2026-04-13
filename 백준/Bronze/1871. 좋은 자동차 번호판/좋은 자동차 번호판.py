N = int(input())

for i in range(N):
    a, b = input().split('-')
    
    num1, num2 = 0, int(b)
    
    for j in range(3):
        num1 += ((ord(a[2 - j]) - 65) * (26 ** j))
    
    if (abs(num1 - num2) <= 100):
        print("nice")
        
    else:
        print("not nice")