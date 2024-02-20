class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}

        def fib(n):
            if n <= 1: 
                return n
            if n == 2:
                return 1
            
            if n not in memo:
                memo[n] = fib(n-3) + fib(n-1) + fib(n-2)

            return memo[n]

        return fib(n)
        
