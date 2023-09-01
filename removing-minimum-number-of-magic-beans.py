class Solution:
    def minimumRemoval(self, beans: List[int]) -> int:
        beans.sort()
        total = sum(beans)
        length = len(beans)
        diff = []
        for i in range(len(beans)):
            diff.append(total - (beans[i] * (length - i)))
        
        return min(diff)
