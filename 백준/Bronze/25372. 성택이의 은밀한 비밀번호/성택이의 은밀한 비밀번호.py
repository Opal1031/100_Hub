N = int(input())

for i in range(N):
	num = input()
    
	if len(num) >= 6 and len(num) <= 9:
		print("yes")
	else:
		print("no")