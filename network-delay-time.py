class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = [[float("inf")] * (n) for _ in range(n)]

        for src, dest, cost in times:
            graph[src-1][dest-1] = cost

        for i in range(n):
            graph[i][i] = 0

        for a in range(n):
            for i in range(n):
                for j in range(n):
                    graph[i][j] = min(graph[i][j], graph[i][a]+graph[a][j])

        return max(graph[k-1]) if max(graph[k-1]) != float("inf") else -1
