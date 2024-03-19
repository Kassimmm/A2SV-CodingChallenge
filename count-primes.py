class Solution:
    def countPrimes(self, n: int) -> int:
        def prime(n):
            arr = [True for _ in range(n)]

            for i in range(2, int(sqrt(n))+1):
                for j in range(i*i, n, i):
                    if j != i and (j %i) == 0:
                        arr[j] = False

            res = 0
            for i in range(2, n):
                if arr[i] == True:
                    res += 1
            return res

        return prime(n)

        
