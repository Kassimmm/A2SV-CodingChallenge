class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        n = len(nums)
        i = 0

        while i < n:
            if 1 <= nums[i] <= n and nums[i] != i+1 and nums[i] != nums[nums[i]-1]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1] 
            else:
                i += 1

        return next((nums[i] for i in range(len(nums)) if nums[i] != i+1), 0)   ## using cyclic sort



# class Solution:
#     def findDuplicate(self, nums: List[int]) -> int: 
#         nums.sort()

#         for i in nums:
#             if (bisect.bisect_right(nums, i)-1) != (bisect.bisect_left(nums, i)):
#                 return i
