class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for i in range(len(rooms)):
            graph[i] = rooms[i]

        def bfs(graph, node):
            queue = deque()
            visited = set()
            queue.append(node)
            visited.add(node)

            while queue:
                n = len(queue)
                for _ in range(n):
                    temp = queue.popleft()
                    for neigh in graph[temp]:
                        if neigh not in visited:
                            visited.add(neigh)
                            queue.append(neigh)
            return len(visited)

        return len(rooms) == bfs(graph, 0)
