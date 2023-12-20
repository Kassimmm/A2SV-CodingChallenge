class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = defaultdict(int)
        for i, j in prerequisites:
            hashmap[i] += 1

        graph = {i: [] for i in range(numCourses)}
        for i, j in prerequisites:
            graph[j].append(i)

        res = []
        queue = deque()
        for key, value in enumerate(graph):
                if key not in hashmap:
                    queue.append(key)

        while queue:
            n = len(queue)
            for _ in range(n):
                temp = queue.popleft()
                res.append(temp)
                
                for node in graph[temp]:
                    hashmap[node] -= 1

                    if hashmap[node] == 0:
                        queue.append(node)
                        
        return res if len(res) == numCourses else []
