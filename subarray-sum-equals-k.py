class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        presum = count = 0
        hashmap = defaultdict(int)
        hashmap[0] = 1

        for r in range(len(nums)):
            presum += nums[r]
            count += hashmap[presum - k]

            hashmap[presum] += 1
        return count




