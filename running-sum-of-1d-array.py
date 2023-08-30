class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runn = [0] * len(nums)
        prefsum = 0
        for i in range(len(nums)):
            prefsum += nums[i]
            runn[i] = prefsum
        return runn
    
