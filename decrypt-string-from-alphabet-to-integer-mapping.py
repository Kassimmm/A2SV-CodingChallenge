class Solution:
    def freqAlphabets(self, s: str) -> str:
        res = []
        right = len(s)-1
        while right > -1 :
            if s[right] != "#":
                res.append(chr( 96 + int(s[right])))
                right -= 1
            else:
                res.append(chr(96 + int(s[right-2] + s[right-1])))
                right -= 3
        ans = res[::-1]     
        return ("".join(ans))
        
