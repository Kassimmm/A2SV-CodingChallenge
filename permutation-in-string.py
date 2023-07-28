class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l,r = 0,len(s1)
        isBool = False
        s1 = Counter(s1)
        while r < len(s2)+1:
            if Counter(s2[l:r]) == s1:
                isBool = True
            l += 1
            r += 1
        return isBool  
