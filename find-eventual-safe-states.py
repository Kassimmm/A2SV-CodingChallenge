class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        hashmap = {i:0 for i in range(len(graph))}
        _graph = {i:[] for i in range(len(graph))}
        res = []
        queue = deque()

        for i in range(len(graph)):
            for j in graph[i]:
                hashmap[i] += 1

        for i in range(len(graph)):
            for j in graph[i]:
                _graph[j].append(i)

        for i in _graph:
            if graph[i] == []:
                queue.append(i)

        while queue:
            n = len(queue)
            for _ in range(n):
                node = queue.popleft()
                res.append(node)

                for i in _graph[node]:
                    hashmap[i] -= 1
                    if hashmap[i] == 0:
                       queue.append(i)
        res.sort()
        return res
                
