A, B = input().split()

A2 = "".join(reversed(A))
B2 = "".join(reversed(B))

if A2 > B2:
    print(A2)

else:
    print(B2)