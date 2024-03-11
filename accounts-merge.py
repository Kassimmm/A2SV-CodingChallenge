class UnionFind:
    def __init__(self, accounts):
        self.parent = defaultdict(str)
        self.size = defaultdict(str)

        for account in accounts:
            for i in range(1, len(account)):
                self.parent[account[i]] = account[i]
                self.size[account[i]] = account[0]


    def find(self, node):
        if node == self.parent[node]: 
            return node
        
        self.parent[node] = self.find(self.parent[node])
        return self.parent[node] 

    def get(self):
        return self.parent
        
    
    def union(self, u, v): 
        root1 = self.find(u) 
        root2 = self.find(v)
        
        if root1 < root2:
            self.parent[root2] = root1
        else:
            self.parent[root1] = root2


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        disjoint = UnionFind(accounts)

        for account in (accounts):
            for i in range(1, len(account)-1):
                disjoint.union(account[i], account[i+1])
        
        graph = defaultdict(list)
        res = []
        for key in disjoint.parent:
            graph[disjoint.find(key)].append(key)

        for item in graph:
            res.append([disjoint.size[item]] + sorted(graph[item]))

        return res
