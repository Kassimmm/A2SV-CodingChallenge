class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = []
        # total = nums[0]
        # for i in range(1, len(nums)):
        #     total = total * nums[i]


        # for i in range(len(nums)):
        #     if nums[i] == 0:
        #         output.append(reduce (lambda x,y: x * y, (nums[:i] + nums[i+1:])))
        #     else:
        #         ans = total // nums[i]
        #         output.append(ans)
        # return output

        """
        the above solution is an optimal approach but I cheated because I used a    division operator
        """
        res = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

