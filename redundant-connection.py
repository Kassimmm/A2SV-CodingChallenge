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
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        graph = UnionFind(len(edges))

        for u, v in edges:
            if graph.find(u-1) == graph.find(v-1) :
                return  [u, v]
            graph.union(u-1, v-1) 

        return res

        
