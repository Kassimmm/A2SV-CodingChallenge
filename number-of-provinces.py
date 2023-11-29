class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = defaultdict(list)
        for i in range(len(isConnected)):
            for j in range(len(isConnected[0])):
                if isConnected[i][j] == 1:
                    graph[i].append(j)
                

        visited, count = set(), 0
        def dfs(node,visited):
            if node in visited:
                return

            visited.add(node)
            for v in graph[node]:
                if v not in visited:
                    dfs(v,visited)      

        for node in graph:
            if node not in visited:
                dfs(node,visited)
                count += 1
        return count 
