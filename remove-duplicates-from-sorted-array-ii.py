from collections import defaultdict
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        l = 0
        hashmap = {}
        while l < n:
            if nums[l] in hashmap:
                hashmap[nums[l]] += 1
            else:
                hashmap[nums[l]] = 1

            if hashmap[nums[l]] > 2:
                nums.append(nums.pop(l))
                l -= 1
                n -= 1
            l += 1


        mydict = defaultdict(int)

        for i in range(len(nums)):
            mydict[nums[i]] += 1

            if mydict[nums[i]] > 2:
                return (i)
                break
            
