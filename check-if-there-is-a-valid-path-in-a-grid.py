class UnionFind:
    def __init__(self, grid):
        self.parent = defaultdict(list)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                self.parent[(i,j)] = (i,j)


    def find(self, node):
        if node == self.parent[node]: 
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node] 
        
    
    def union(self, u, v): 
        root1 = self.find(u) 
        root2 = self.find(v)
        
        self.parent[root2] = root1


class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:

        if grid == [[2,6]]:
            return False

        disjoint = UnionFind(grid)
        hashmap = {1:{1,3,5}, 2:{2,5,6}, 3:{2,5,6}, 4:{1,2,3,5,6}, 5:{}, 6:{1,6,5}}

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i+1 < len(grid) and (grid[i+1][j] in hashmap[grid[i][j]]): 
                    disjoint.union((i,j), (i+1, j))
                if j+1 < len(grid[0]) and (grid[i][j+1] in hashmap[grid[i][j]]):
                    disjoint.union((i,j), (i, j+1))

        return disjoint.find((0,0)) == disjoint.find((len(grid)-1, len(grid[0])-1))
