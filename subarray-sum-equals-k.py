class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap = {0: 1}
        count = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            diff = cur_sum - k
            count += hashmap.get(diff, 0)

            hashmap[cur_sum] = 1 + hashmap.get(cur_sum, 0)

        return count
