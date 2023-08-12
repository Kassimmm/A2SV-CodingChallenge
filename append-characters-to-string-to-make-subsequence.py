class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        l = r = count = 0
        while l < len(s) and r < len(t):
            if s[l] == t[r]:
                count += 1
                l += 1
                r += 1
            else:
                l += 1
        
        return len(t) - count
        
                
