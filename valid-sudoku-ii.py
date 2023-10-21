class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        nums = []

        for i in range(rows):
            for j in range(cols):
                elem = board[i][j]
                if elem != '.':
                    row = (elem, i)
                    column = (j, elem)
                    subgrid = (i // 3, j // 3, elem)

                    nums.append(row)
                    nums.append(column)
                    nums.append(subgrid)

        return len(nums) == len(set(nums))

