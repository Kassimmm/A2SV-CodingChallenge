class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        while l <= r:
            m = (l+r) // 2
            if guess(m) == -1:
                r = m-1
            elif guess(m) == 1:
                l = m+1
            else:
                return m
