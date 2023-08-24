class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        new_s = s + s
        
        if s in new_s[1:-1]:
            return True
        return False
        
