class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [-1] * (n+1)
        
        def dfs(node):
            for hater in graph[node]:
                if color[node] == color[hater]:
                    return False
                if color[hater] == -1:
                    if color[node] == 0:
                        color[hater] = 1
                    else:
                        color[hater] = 0
                    if not dfs(hater):
                        return False
            return True

        res = True
        for node in graph:
            if color[node] == -1:
                color[node] = 0
                res = res and dfs(node)
        return res
