import sys

N = int(sys.stdin.readline())
next_ask = [0] * (N + 1)
len_count = 0
ask_to_who = 0

for i in range(1, N + 1):
    next_ask[i] = int(sys.stdin.readline())

for j in range(1, N + 1):
    ans = []
    ans.append(j)

    while True:
        ans.append(next_ask[ans[-1]])

        if ans.count(ans[-1]) == 2:
            break

    if len(ans) > len_count:
        len_count = len(ans)
        ask_to_who = j

print(ask_to_who)