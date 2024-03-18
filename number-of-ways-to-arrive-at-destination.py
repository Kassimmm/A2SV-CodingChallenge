class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)
        for u, v, time in roads:
            graph[u].append([v, time])
            graph[v].append([u, time])
        
        visited = set()
        heap = [(0,0)]
        heapify(heap)

        res = defaultdict(int)

        while heap:
            cost, node = heappop(heap)

            if node in visited:
                continue

            res[node] = cost
            visited.add(node)

            for child in graph[node]:
                if child[0] not in visited:
                    heappush(heap, (cost+child[1], child[0]))

        target = res[n-1]

        memo = {}
        def dfs(node, count):
            if (node, count) in memo:
                return memo[(node, count)]

            if node == 0: 
                return 1

            ans = 0
            for child in graph[node]:
                if res[child[0]] + count + child[1] == target: 
                    ans += dfs(child[0], count + child[1])
            memo[(node, count)] = ans

            return memo[(node, count)]

        return dfs(n-1, 0) % ((10 ** 9)+7)
