class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(total):
            if total in memo:
                return memo[total]

            if total == target:
                return 1

            res = 0
            if total not in memo:
                for num in nums:
                    if total + num <= target:
                        res += dp(total + num)

                memo[total] = res
            
            return memo[total]

        return dp(0)

        
