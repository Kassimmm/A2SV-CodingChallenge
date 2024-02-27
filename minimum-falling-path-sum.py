class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}

        def dp(i,j):
            if (i,j) in memo:
                return memo[(i,j)]

            if 0 <= i < len(matrix) and 0 <= j < len(matrix[0]) and i == len(matrix)-1:
                return matrix[i][j]

            if j < 0 or j == len(matrix[0]):
                return float("inf")

            if (i,j) not in memo:
                left =  matrix[i][j] + dp(i+1, j-1)  
                right = matrix[i][j] + dp(i+1, j+1)
                down =  matrix[i][j] + dp(i+1, j) 
                memo[(i,j)] = min(left, right, down)

            return memo[(i,j)]

        res = float("inf")
        for j in range(len(matrix[0])):
            res = min(res, dp(0,j))

        return res
