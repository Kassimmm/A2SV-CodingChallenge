class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        s = s[::-1]
        m = len(s)
        res = 0
        p = pow(power, k - 1, modulo)
        
        temp = 0
        for i in range(k):
            temp = (temp * power + (ord(s[i]) - 96)) % modulo
        
        if temp == hashValue: 
            res = s[:k][::-1]
        
        for i in range(k, m):
            temp = (temp - (ord(s[i - k]) - 96) * p) % modulo
            temp = (temp * power + (ord(s[i]) - 96)) % modulo
            
            if temp == hashValue: 
                res = s[i - k + 1:i + 1][::-1]
        
        return res
