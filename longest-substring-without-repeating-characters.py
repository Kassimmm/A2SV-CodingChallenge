class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        l = ans = 0

        for r in range(len(s)):
            while s[r] in hashset:
                hashset.remove(s[l])
                l += 1
            hashset.add(s[r])
            ans = max(ans, len(hashset))
            
        return (ans)
