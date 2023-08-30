class NumArray:
    def __init__(self, nums: List[int]):
        self.pre_arr = [0] * len(nums)
        self.pre_arr[0] = nums[0]
        for i in range(1, len(nums)):
            self.pre_arr[i] = self.pre_arr[i-1] + nums[i]
            
    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.pre_arr[right]
        else:
            return self.pre_arr[right] - self.pre_arr[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
