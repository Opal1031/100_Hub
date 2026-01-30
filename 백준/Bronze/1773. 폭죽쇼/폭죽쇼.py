import sys
 
N, C = map(int, sys.stdin.readline().split())
firework = [0] * (C + 1)
 
for _ in range(N):
    time = int(sys.stdin.readline())
    
    if (time == 1):
        print(C)
        exit()
        
    else:
        for i in range(time, C + 1, time):
            firework[i] = 1
 
print(sum(firework))