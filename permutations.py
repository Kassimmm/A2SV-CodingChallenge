class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        if len(nums) == 1:
            return [nums[:]]

        for i in range(len(nums)):
            num = nums.pop(0)
            temp = self.permute(nums)
            for item in temp:
                item.append(num)
            result.extend(temp)
            nums.append(num)
        return result
