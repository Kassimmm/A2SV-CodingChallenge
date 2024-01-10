class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        temp = [0] * (len(nums)+1)

        for i in range(len(nums)):
            t = nums[i]
            temp[t] += 1

        for i in range(len(temp)):
            if temp[i] == 0:
                return i
