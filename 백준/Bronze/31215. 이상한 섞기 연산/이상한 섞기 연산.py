import sys

data = sys.stdin.read().split()

if data:
	t = int(data[0])
	out = []

	for i in range(1, t + 1):
		n = int(data[i])
		out.append("1" if n <= 2 else "3")

	sys.stdout.write("\n".join(out))