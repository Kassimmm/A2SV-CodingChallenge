class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        memo = {}

        def dp(left, right, turn):
            if (left, right, turn) in memo:
                return memo[(left, right, turn)]
            if left > right:
                return 0

            if turn:
                select_L = nums[left] + dp(left+1, right, not turn)
                select_R = nums[right] + dp(left, right-1, not turn)

                memo[(left, right, turn)] = max(select_L, select_R)
            else:
                select_L = -nums[left] + dp(left+1, right, not turn)
                select_R = -nums[right] + dp(left, right-1, not turn)

                memo[(left, right, turn)] = min(select_L, select_R)

            return memo[(left, right, turn)]

        return dp(0, len(nums)-1, True) >= 0
