class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[float("inf")] * (numCourses) for _ in range(numCourses)]

        for src, dest in prerequisites:
            graph[src][dest] = 1

        for i in range(numCourses):
            graph[i][i] = 0

        for a in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    graph[i][j] = min(graph[i][j], graph[i][a]+graph[a][j])
        
        res = []

        for i, j in queries:
            res.append(graph[i][j] != float("inf"))
        
        return res

        

        

        
