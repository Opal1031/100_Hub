CRO = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

str = input()

for i in CRO:
    str = str.replace(i, "X")

print(len(str))