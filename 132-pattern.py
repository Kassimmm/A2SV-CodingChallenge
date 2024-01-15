class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        mini = float("inf")

        for i in range(len(nums)):
            while stack and nums[i] >= stack[-1][0]:
                stack.pop()
                
            if stack and nums[i] < stack[-1][0] and nums[i] > stack[-1][1]:
                return True 
            
            stack.append([nums[i], mini])
            mini = min(mini, nums[i])

        return False
