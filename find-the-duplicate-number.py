class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        nums.sort()

        for i in nums:
            if (bisect.bisect_right(nums, i)-1) != (bisect.bisect_left(nums, i)):
                return i
