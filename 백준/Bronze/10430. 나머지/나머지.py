A, B, C = map(int, input().split())

print((A + B) % C, end = "\n")
print(((A % C) + (B % C)) % C, end = "\n")
print((A * B) % C, end = "\n")
print(((A % C) * (B % C)) % C)