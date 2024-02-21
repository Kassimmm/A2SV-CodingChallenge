class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        nums1, nums2 = nums[1:], nums[:-1]

        def dp(i, arr,memo):
            if i >= len(arr):
                return 0

            if i not in memo:
                memo[i] = max(dp(i+1, arr, memo), arr[i]+dp(i+2, arr, memo)) 

            return memo[i] 
        
        return max(dp(0, nums1, {}), dp(0, nums2, {}))
