class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        n = len(edges)
        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            if len(graph[edge[0]]) > (n-1):
                return edge[0]
            if  len(graph[edge[1]]) > (n-1):
                return edge[1]
