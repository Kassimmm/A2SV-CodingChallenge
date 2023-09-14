class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        bl, br = -1, -1
        left, right = 0, len(nums)-1

        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
            else:
                bl = mid
                right = mid -1

        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right + left) // 2

            if nums[mid] > target:
                right = mid-1
            elif nums[mid] < target:
                left = mid + 1
            else:
                br = mid
                left = mid +1

        return [bl, br]
