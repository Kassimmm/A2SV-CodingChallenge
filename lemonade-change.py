class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = defaultdict(int)
        for bill in bills:
            change[bill] += 1

            if bill == 10:
                if change[5] == 0:
                    return False
                else:
                    change[5] -= 1
            
            if bill == 20:
                if change[5] >= 1 and change[10] >= 1:
                    change[10] -= 1
                    change[5] -= 1
                elif change[10] == 0 and change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True
        
