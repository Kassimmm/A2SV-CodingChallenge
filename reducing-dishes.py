class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        res = 0
        satisfaction.sort() 

        for i in range(len(satisfaction)-1,-1,-1):
            total = 0
            k = 1
            for j in range(i, len(satisfaction)):
                total += (k) * satisfaction[j]
                k += 1
            
            res = max(res, total)

        return res       

        
