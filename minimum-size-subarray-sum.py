class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minSize = float("inf")
        left, currSum = 0, 0

        for right in range(len(nums)):
            currSum += nums[right]
            while currSum >= target:
                minSize = min(minSize, right-left+1)
                currSum -= nums[left]
                left += 1
                
        return 0 if minSize == float("inf") else minSize
