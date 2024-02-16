class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count = 0
        resx, resy = [], []

        while x > 0:
            resx.append(x & 1)
            x >>= 1
        
        while y > 0:
            resy.append(y & 1)
            y >>= 1

        n = min(len(resx), len(resy))

        for i in range(n):
            if resx[i] != resy[i]:
                count += 1

        if resx[n:]:
            count += resx[n:].count(1)
        else:
            count += resy[n:].count(1)

        return count


        
