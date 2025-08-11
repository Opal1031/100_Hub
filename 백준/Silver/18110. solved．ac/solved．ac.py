import sys

N = int(sys.stdin.readline())

if (N == 0):
    print(0)
    sys.exit()

score = [0 for _ in range(N)]

for i in range(N):
    score[i] = int(sys.stdin.readline())

score.sort()

trim = int(N * 0.15 + 0.5)
trimmed_scores = score[trim : N - trim]

if len(trimmed_scores) == 0:
    print(0)

else:
    avg = (sum(trimmed_scores) / len(trimmed_scores))
    print(int(avg + 0.5))