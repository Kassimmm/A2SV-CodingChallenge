class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        ans = [0] * len(shifts)
        total = 0
        res = []

        for i in range(len(shifts)-1,-1,-1):
            total += shifts[i]
            ans[i] = total
            
        for i in range(len(shifts)):
            shifts[i] = (ord(s[i])-ord('a') + ans[i])%26

        for i in range(len(shifts)):
            res.append(chr(shifts[i]+ord('a')))

        return "".join(res)
