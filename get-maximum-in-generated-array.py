class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        
        memo = [-1 for _ in range(n+1)] 
        memo[0], memo[1] = 0, 1

        def helper(n):
            if n <= 1:
                return n

            if memo[n] == -1:
                if n % 2 == 0:
                    memo[n] = helper(n // 2)
                else:
                    memo[n] = helper(n // 2) + helper((n // 2) + 1)
            return memo[n]

        for i in range(n+1):
            helper(i)

        return max(memo)
