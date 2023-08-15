class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = [0] * len(nums)
        right = [0] * len(nums)
        answer = [0] * len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
            
        for j in range(len(nums)-2, -1, -1):
            right[j] = right[j+1] + nums[j+1]
            
        l = 0
        while l < len(nums):
            answer[l] = abs(left[l] - right[l])
            l += 1
            
        return answer
