class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        hashmap = defaultdict(int)
        graph = defaultdict(list)
        queue = deque()
        res = defaultdict(set)
        output = []

        for i, j in edges:
            hashmap[j] += 1

        for  i, j  in edges:
            graph[i].append(j)

        for i in range(n):
            if i not in hashmap:
                queue.append(i)

        while queue:
            k = len(queue)
            for _ in range(k):
                node = queue.popleft()
                for i in graph[node]:
                    res[i].add(node)
                    res[i].update(res[node])
                    
                    hashmap[i] -= 1
                    if hashmap[i] == 0:
                        queue.append(i)

        for i in range(n):
            output.append(sorted(list(res[i])))

        return output
