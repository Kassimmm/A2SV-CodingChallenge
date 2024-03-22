class Solution:
    def longestPrefix(self, s: str) -> str:
        base = 31
        m = len(s)
        mod = ((10 ** 9)+7)
        res = ""
        hash1 = (ord(s[0]) - 96) % mod
        hash2 = (ord(s[-1]) - 96) % mod 

        for i in range(1, len(s)-1):
            if hash1 == hash2: res = s[:i]

            hash1 *= 31
            hash1 += (ord(s[i])-96)
            hash1 %= mod

            hash2 += ((ord(s[m-i-1])-96) * base)
            hash2 %= mod
            base *= 31
            base %= mod

        if hash1 == hash2: res = s[:m-1]

        return res
        
