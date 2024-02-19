class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        res = []
        output, path = [], []
        def back(i):
            if i == len(nums):
                output.append(path.copy())
                return
            path.append(nums[i])
            back(i+1)
            path.pop()
            back(i+1)
        
        back(0)
                
        for i in output:
            if i:
                x = i[0]
                for j in range(len(i)):
                    x |= i[j]
                res.append(x)
        
        return res.count(max(res))

