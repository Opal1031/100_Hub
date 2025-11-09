n = input()
str = input()

str_count = []

for i in str:
    if(i !=',') and (i != ' '):
        str_count.append(str.count(i))

print(max(str_count))