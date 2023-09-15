class Solution:
    def findDuplicate(self, nums: List[int]) -> int: 
        hashmap = defaultdict(int)
        for i in range(len(nums)):
            hashmap[nums[i]] += 1
            if hashmap[nums[i]] > 1:
                return nums[i] 
