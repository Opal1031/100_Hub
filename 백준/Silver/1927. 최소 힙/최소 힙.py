import sys
import heapq
input = sys.stdin.readline

N = int(input())

heap = []

for _ in range(N):
    x = int(input())

    if (x == 0):
        print(heapq.heappop(heap) if heap else 0)

    else:
        heapq.heappush(heap, x)