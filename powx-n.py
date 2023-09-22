class Solution:
    def myPow(self, x: float, n: int) -> float:
        def power(x, n):
            if n == 0:
                return 1
            if n == 1:
                return x

            res = power(x, abs(n)//2) 
            ans = res * res

            return x * ans if n % 2 else ans 

        result = power(x, abs(n))
        return 1/result if n < 0 else result
