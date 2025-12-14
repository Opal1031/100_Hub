import sys

N, M = map(int, sys.stdin.readline().split())

total_minutes = (M * 1440) // N
hours, minutes = divmod(total_minutes, 60)

print(f"{hours:02d}:{minutes:02d}")