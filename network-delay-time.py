class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for src, dest, cost in times:
            graph[src].append((dest, cost))

        def dp(source, destination):
            visited = set()
            heap = [(0,source)]
            heapify(heap)

            while heap:
                cost, node = heappop(heap)

                if node == destination:
                    return cost

                visited.add(node)

                for child in graph[node]:
                    if child[0] not in visited:
                        heappush(heap, (cost+child[1], child[0]))

            return -1

  
        res = []
        for i in range(1, n+1): 
            res.append(dp(k, i))

        if -1 in res:
            return (-1)
        else:
            return (max(res))

        
