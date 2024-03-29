class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        left, right = 0, len(height)-1

        while left < right:
            k = min(height[left], height[right])
            res = max(res, (right-left)* k)
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return res
