g, p, t = map(int, input().split())

kit = p * (g - t)

if kit < g:
    print("1")
elif kit > g:
    print("2")
else:
    print("0")