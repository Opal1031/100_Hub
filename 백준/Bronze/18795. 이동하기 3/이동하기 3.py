import sys

n, m = map(int, sys.stdin.readline().split())

a_list = list(map(int, input().split()))
b_list = list(map(int, input().split()))

print(sum(a_list) + sum(b_list))