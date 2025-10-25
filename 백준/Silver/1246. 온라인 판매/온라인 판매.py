import sys

N, M = map(int, sys.stdin.readline().split())
buyers = [int(sys.stdin.readline()) for _ in range(M)]

buyers.sort()

max_revenue = 0
answer_price = 0

for i in range(M):
    price = buyers[i]
    sell = min(N, M - i)

    revenue = price * sell
    
    if (revenue > max_revenue):
        max_revenue = revenue
        answer_price = price

print(answer_price, max_revenue)