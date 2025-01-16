table = []

for i in range(9):
    row = list(map(int, input().split()))
    table.append(row)

num_max = 0
max_row, max_col = 0, 0

for row in range(9):
    for col in range(9):
        if num_max <= table[row][col]:
            max_row, max_col = row + 1, col + 1
            num_max = table[row][col]

print(num_max)
print(max_row, max_col)