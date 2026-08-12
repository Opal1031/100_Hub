import heapq

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]

    for start, end, cost in fares:
        graph[start].append((end, cost))
        graph[end].append((start, cost))

    def dijkstra(start):
        distance = [float('inf')] * (n + 1)
        distance[start] = 0

        heap = [(0, start)]

        while heap:
            current_distance, current = heapq.heappop(heap)

            if (distance[current] < current_distance):
                continue

            for next_node, cost in graph[current]:
                new_distance = current_distance + cost

                if (new_distance < distance[next_node]):
                    distance[next_node] = new_distance
                    heapq.heappush(heap, (new_distance, next_node))

        return distance

    from_start = dijkstra(s)
    from_a = dijkstra(a)
    from_b = dijkstra(b)

    answer = float('inf')

    for split in range(1, n + 1):
        total = from_start[split] + from_a[split] + from_b[split]
        answer = min(answer, total)

    return answer