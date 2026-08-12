import heapq

def solution(N, road, K):
    graph = [[] for _ in range(N + 1)]

    for start, end, cost in road:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    distance = [float('inf')] * (N + 1)
    distance[1] = 0

    heap = [(0, 1)]

    while heap:
        current_distance, current = heapq.heappop(heap)

        if (distance[current] < current_distance):
            continue

        for next_node, cost in graph[current]:
            new_distance = current_distance + cost

            if (new_distance < distance[next_node]):
                distance[next_node] = new_distance
                heapq.heappush(heap, (new_distance, next_node))

    return sum(1 for value in distance[1:] if value <= K)