class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, curr):
            if i == len(nums):
                return int(curr == target)

            if (i, curr) not in memo:
                a = dp(i+1, -nums[i]+curr)
                b = dp(i+1, nums[i]+curr)
                memo[(i, curr)] = a+b

            return memo[(i, curr)]

        return dp(0,0)
