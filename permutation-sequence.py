class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        nums = [i for i in range(1, n+1)]
        res, path = [], []

        def back():
            if len(path) == len(nums):
                res.append(path.copy())
                return 

            if len(res) == k:
                return 

            for num in nums:
                if num not in path:
                    path.append(num)
                    back()
                    path.pop()

        back()

        return "".join(map(str, res[-1]))
