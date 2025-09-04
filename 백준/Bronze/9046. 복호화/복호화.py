import sys

T = int(sys.stdin.readline())

for _ in range(T):
    s = sys.stdin.readline().replace(" ", "").strip().lower()
    count_s = [0] * 26

    for i in s:
        if "a" <= i <= "z":
            count_s[ord(i) - 97] += 1

    if count_s.count(max(count_s)) > 1:
        print("?")

    else:
        print(chr(97 + count_s.index(max(count_s))))