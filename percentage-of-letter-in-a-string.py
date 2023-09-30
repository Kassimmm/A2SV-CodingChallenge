class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        target = ord(letter)
        for i in s:
            if ord(i) == target:
                count += 1
        res = (count / len(s)) * 100
        return math.floor(res)
