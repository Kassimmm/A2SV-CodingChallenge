class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(amount):
            if amount == 0:
                return 0
            if amount < 0:
                return float("inf")

            mini = float("inf")
            for i in range(len(coins)):
                mini = min(mini, 1+ dp(amount-coins[i])) 

            return mini

        return dp(amount) if dp(amount) != float("inf") else -1
