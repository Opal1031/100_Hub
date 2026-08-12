def solution(n, computers):
    visited = [False] * n

    def dfs(current):
        visited[current] = True

        for next_node in range(n):
            if (computers[current][next_node] == 1 and not visited[next_node]):
                dfs(next_node)

    answer = 0

    for node in range(n):
        if not visited[node]:
            dfs(node)
            answer += 1

    return answer