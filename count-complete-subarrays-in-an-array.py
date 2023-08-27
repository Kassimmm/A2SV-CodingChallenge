class Solution:
    def countCompleteSubarrays(self, nums: List[int]) -> int:
        target = len(set(nums))
        hashmap = defaultdict(int)
        l = ans = 0
        for r in range(len(nums)):
            hashmap[nums[r]] += 1
            while len(hashmap) >= target:
                hashmap[nums[l]] -= 1
                if hashmap[nums[l]] == 0:
                    del hashmap[nums[l]]
                l += 1
            ans += l
        return ans

            
