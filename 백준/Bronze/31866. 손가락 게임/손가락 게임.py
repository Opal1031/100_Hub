A, B = input().split()
 
if A in ("0", "2", "5") and B not in ("0", "2", "5"):
    print(">")
elif A not in ("0", "2", "5") and B in ("0", "2", "5"):
    print("<")
elif (A, B) in (("0", "2"), ("2", "5"), ("5", "0")):
    print(">")
elif (A, B) in (("2", "0"), ("5", "2"), ("0", "5")):
    print("<")
else:
    print("=")