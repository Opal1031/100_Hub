import sys

T1 = int(sys.stdin.readline().strip())
T2 = int(sys.stdin.readline().strip())
sleep_time = T2 - T1

if (sleep_time < 0):
    sleep_time += 24

print(sleep_time)