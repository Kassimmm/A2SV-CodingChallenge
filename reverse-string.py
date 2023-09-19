class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        mid = len(s) // 2
        left, right = 0, len(s)-1

        def reverse(s, left, right):
            if left == mid:
                return s
            s[left], s[right] = s[right], s[left]
            return reverse(s, left+1, right-1)

        return reverse(s, left, right)
