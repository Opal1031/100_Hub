N, M, S = map(int, input().split())
 
N_Percent = S * (M + 1) * (100 - N) // 100
M_Plus_One = S * M
 
print(min(N_Percent, M_Plus_One))