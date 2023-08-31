class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        presum = count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1

        for r in range(len(nums)):
            presum = (presum + nums[r]) % k
            count += hashmap[presum]

            hashmap[presum] += 1

        return count
