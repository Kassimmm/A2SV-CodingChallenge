class Solution:
    def findComplement(self, num: int) -> int:
        res = []
        while num > 0:
            res.append(num & 1)
            num >>= 1

        res = [1-i for i in res]
        res = res[::-1]
        return int("".join(map(str, res)), 2)
        
