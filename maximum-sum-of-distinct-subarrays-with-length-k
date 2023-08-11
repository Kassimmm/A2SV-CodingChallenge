class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
            hashmap = defaultdict(int)
            currSum = maxSum = 0

            if k <= 0 or len(nums) < k: 
                return 0

            for r in range(k):
                hashmap[nums[r]] += 1
                currSum += nums[r]

            if len(hashmap) == k:
                maxSum = currSum

            for r in range(k, len(nums)):
                hashmap[nums[r]] += 1
                currSum -= nums[r-k]

                hashmap[nums[r-k]] -= 1

                if hashmap[nums[r-k]] == 0:
                    hashmap.pop(nums[r-k])

                currSum += nums[r]
                if len(hashmap) == k:
                    maxSum = max(maxSum, currSum)

            return maxSum
