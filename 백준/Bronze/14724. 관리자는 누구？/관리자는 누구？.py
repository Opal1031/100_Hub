club_name_list = ["PROBRAIN", "GROW", "ARGOS", "ADMIN", "ANT", "MOTION", "SPG", "COMON", "ALMIGHTY"]

D = dict()
n = int(input())
ans = ""
temp = 0

for idx in range(9):
    score_list = list(map(int, input().split()))
    D[club_name_list[idx]] = max(score_list)
    
    if (D[club_name_list[idx]] > temp):
        temp = D[club_name_list[idx]]
        ans = club_name_list[idx]
        
print(ans)