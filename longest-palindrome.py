class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        occurence = Counter(s)
        flag = False
        
        for key, value in occurence.items():

            if value % 2 == 0:
                res += value

            else:
                flag = True
                res += value-1

        if flag:
            res += 1

        return res
  


                
    
            
            
        
