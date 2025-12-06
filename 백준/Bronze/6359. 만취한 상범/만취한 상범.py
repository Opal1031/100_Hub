import sys

T = int(sys.stdin.readline())

for _ in range(T):
    n = int(sys.stdin.readline())
    answer = 0 

    for i in range(1, n):
        if (i ** 2 <= n):
            answer += 1

        else:
            break
            
    print(answer)