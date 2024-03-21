class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def hash(string):
            res = 0
            for i in range(len(string)):
                res += (ord(string[i]) - 96) * (26 ** (n-i-1))
            return res % ((10 ** 9)+7)  

        def add(char, code):
            code *= 26
            code += (ord(char)-96)
            return code % ((10 ** 9)+7)

        def remove(char, code):
            code -= (26 ** (n-1)) * (ord(char) - 96)
            return code % ((10 ** 9)+7)

        m, n = len(haystack), len(needle)
        temp = hash(haystack[:n])
        target = hash(needle)
        if temp == target:
            return 0

        for i in range(n, m):
            temp = remove(haystack[i-n], temp)
            temp = add(haystack[i], temp)

            if temp == target:
                return (i-n+1)

        return -1
