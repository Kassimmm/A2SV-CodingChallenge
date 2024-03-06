class UnionFind:
    def __init__(self):
        self.parent = [chr(97+i)for i in range(26)]
        self.size = [chr(97+i)for i in range(26)]


    def find(self, node):
        if node == self.parent[ord(node)-97]: 
            return node
        
        self.parent[ord(node)-97] = self.find(self.parent[ord(node)-97])
        return self.parent[ord(node)-97] 
        
    
    def union(self, u, v):
        root1 = self.find(u) 
        root2 = self.find(v)
        
        if root1 != root2:
            if self.size[ord(root1)-97] > self.size[ord(root2)-97]:
                self.parent[ord(root1)-97] = root2
                self.size[ord(root1)-97] = self.size[ord(root2)-97]
            else:
                self.parent[ord(root2)-97] = root1
                self.size[ord(root2)-97] = self.size[ord(root1)-97]



class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        graph = UnionFind()

        for i in range(len(s1)):
            graph.union(s1[i], s2[i])

        output = []

        for i in range(len(baseStr)):
            output.append(graph.find(baseStr[i]))

        return "".join(output)

         
