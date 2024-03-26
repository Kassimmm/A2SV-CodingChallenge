class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def solve(string):
            s = b + "#" + string
            n, m = len(s), len(b)

            lps = [0] * n
            count = 0

            for i in range(1, n):
                j = lps[i-1]
                
                while j > 0 and s[i] != s[j]:
                    j = lps[j-1]
                
                if s[i] == s[j]:
                    j += 1
                
                if j == m:
                    return 1
                    
                lps[i] = j

            return 0

        k = (len(b) // len(a))

        for i in range(k,k+3):
            string = a * i
            if solve(string):
                return i

        return -1
