import sys

while True:
    N = int(sys.stdin.readline())

    if (N == 0):
        break

    text = list(sys.stdin.readline().strip().upper().replace(" ", ""))

    Cipher = [""] * len(text)
    start_idx = 0
    now_idx = 0

    for i in range(len(text)):
        if (now_idx >= len(text)):
            start_idx += 1
            now_idx = start_idx

        Cipher[now_idx] = text[i]
        now_idx += N  

    print("".join(Cipher))