class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        def fun(n):
            if n == 1:
                return 1
            if n == 2:
                return 2
            if n == 3:
                return 3
            return self.climbStairs(n-1) + self.climbStairs(n-2)
        return fun(n)
