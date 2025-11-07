t = int(input())

for _ in range(t):
    line = input()
    
    if 'D' in line:
        print(line.find('D'))
    else:
        print(len(line))