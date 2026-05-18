from collections import defaultdict

def solution(tickets):
    graph = defaultdict(list)

    for a, b in tickets:
        graph[a].append(b)

    for k in graph:
        graph[k].sort()

    route = ['ICN']
    N = len(tickets) + 1

    def dfs(curr):
        if (len(route) == N):
            return True
        
        if curr not in graph or not graph[curr]:
            return False

        dests = graph[curr]

        for i in range(len(dests)):
            dest = dests.pop(i)
            route.append(dest)

            if dfs(dest):
                return True
            
            route.pop()
            dests.insert(i, dest)

        return False

    dfs('ICN')

    return route