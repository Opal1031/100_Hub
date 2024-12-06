student = []

for a in range(30):
    student.append(a + 1)

for b in range(28):
    student.remove(int(input()))

print(student[0])
print(student[1])