import sys

N, D = map(int, sys.stdin.readline().split())

for _ in range(N):
    result = ""
    word = sys.stdin.readline().strip()

    if (D == 1):
        for i in word:
            if i == "d":
                result += "q"
            elif i == "q":
                result += "d"
            elif i == "b":
                result += "p"
            elif i == "p":
                result += "b"

    elif (D == 2):
        for i in word:
            if i == "d":
                result += "b"
            elif i == "b":
                result += "d"
            elif i == "q":
                result += "p"
            elif i == "p":
                result += "q"
                
    print(result)