class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def func(n):
            if n == 0:
                return [1]
            if n == 1:
                return [1,1]

            res = func(n-1)
            ans = deque()
            for i in range(len(res)-1):
                ans.append(res[i] + res[i+1])
            ans.appendleft(1)
            ans.append(1)
            return list(ans)
            
        return func(rowIndex)
