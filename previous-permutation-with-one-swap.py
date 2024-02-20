class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        n = len(arr)
        i = 0
        for j in range(n-1, 0, -1):
            if arr[j] < arr[j-1]:
                i = j
                break
        
        if i == 0:
            return arr 
        
        maxi = -1
        max_index = -1
        for j in range(i, n):
            if arr[j] < arr[i - 1] and arr[j] > maxi:
                maxi = arr[j]
                max_index = j
        
        arr[i - 1], arr[max_index] = arr[max_index], arr[i - 1]
        
        return arr
