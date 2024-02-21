class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        grid = [[0]* n for _ in range(m)]
        
        def dp(i,j):
            if i == m-1  and j == n-1:
                return 1
            if i == m  or j == n:
                return 0
            if (i,j) not in memo:
                a = dp(i+1, j)
                b = dp(i, j+1)
                memo[(i,j)] = a + b

            return memo[(i,j)]
            
        return dp(0,0)
        
