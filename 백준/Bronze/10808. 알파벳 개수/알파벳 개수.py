S = input()
D = {}

for c in S:
    D[c] = D.get(c, 0) + 1
    
for c in range(97, 123):
    print(D.get(chr(c), 0), end = ' ')