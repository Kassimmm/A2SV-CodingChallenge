class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums)-1
        best = nums[-1]

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                best = min(best, nums[mid])
                right = mid - 1

        return best
