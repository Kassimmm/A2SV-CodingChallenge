class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        res = []
        while n > 0:
            res.append(n & 1)
            n >>= 1

        for i in range(len(res)-1):
            if res[i] == res[i+1]:
                return False
        
        return True
        
