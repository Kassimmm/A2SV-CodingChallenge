class UnionFind:
    def __init__(self, size):
        self.parent = [i for i in range(size)]
        self.size = [1] * size


    def find(self, node):
        if node == self.parent[node]:
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
        
    
    def union(self, u, v):
        root1 = self.find(u)
        root2 = self.find(v)
        
        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.parent[root2] = root1
                self.size[root1] += self.size[root2]
            else:
                self.parent[root1] = root2
                self.size[root2] += self.size[root1]



class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        graph = UnionFind(len(isConnected))

        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]:
                    graph.union(i, j)
        
        res = 0
        visited = set()

        for i in range(len(isConnected)):
            if graph.find(i) not in visited:
                visited.add(graph.find(i))
                res += 1

        print(visited)
        return res       
