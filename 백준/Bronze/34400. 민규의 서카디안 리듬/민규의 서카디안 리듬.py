for _ in range(int(input())):
    time = int(input())
    print("ONLINE" if time % 25 < 17 else "OFFLINE")