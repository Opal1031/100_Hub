N, M = map(int, input().split())
citizenList = input().split()
friends = input().split()
 
result = 0
for c in citizenList[:M]:
    if c not in friends:
        result += 1
 
print(result)