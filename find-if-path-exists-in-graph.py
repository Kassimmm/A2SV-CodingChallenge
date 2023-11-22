class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for i in edges:
            graph[i[0]].append(i[1])
            graph[i[1]].append(i[0])

        def dfs(vertex, visited):
            if vertex == destination:
                return True
            if vertex in visited:
                return False
            visited.add(vertex)
            for neighbour in graph[vertex]:
                temp = dfs(neighbour, visited)
                if temp:
                    return True
            return False
        return dfs(source, set())
