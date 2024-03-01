class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        memo = {}

        def dp(i, status):
            if (i, status) in memo:
                return memo[(i, status)]

            if i == len(prices):
                return 0

            if status:
                buy = -prices[i] + dp(i+1, 0)
                n_buy = dp(i+1, 1)
                memo[(i, status)] = max(buy, n_buy)
            else:
                sell = prices[i]-fee + dp(i+1, 1)
                n_sell = dp(i+1, 0)
                memo[(i, status)] = max(sell, n_sell)

            return memo[(i, status)]
            
        return dp(0, 1)

            
        
        
