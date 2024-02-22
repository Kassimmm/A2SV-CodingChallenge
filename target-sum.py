class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        prev = {0:1}

        for num in nums:
            curr = defaultdict(int)
            for subp in prev:
                curr[subp + num] += prev[subp]
                curr[subp - num] += prev[subp]
            
            prev = curr

        return prev[target] 
