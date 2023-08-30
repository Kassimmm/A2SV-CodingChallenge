class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.presum = [[0] * (len(matrix[0])+1) for _ in range(len(matrix)+1)]

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                self.presum[r+1][c+1] = self.presum[r+1][c] + self.presum[r][c+1] - self.presum[r][c] + matrix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.presum[row2+1][col2+1] - self.presum[row2+1][col1] - self.presum[row1][col2+1] + self.presum[row1][col1]
