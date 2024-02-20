class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = {}

        def dp(i, target):
            if i == len(nums):
                if target == sum(nums) // 2:
                    return True
                if target != sum(nums) // 2:
                    return False


            if (i, target) not in memo:
                memo[(i, target)] = dp(i+1, target+nums[i]) or dp(i+1, target)

            return memo[(i, target)]

        return sum(nums) % 2 == 0 and dp(0, 0)
        
