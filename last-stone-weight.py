class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-i for i in stones]
        heapify(stones)

        while len(stones) > 1:
            y = abs(heappop(stones))
            x = abs(heappop(stones))
            heappush(stones, (x-y))
        return abs(stones[0])
        
