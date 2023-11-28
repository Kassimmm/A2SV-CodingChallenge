from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        res = 0

        def dfs(i, j):
            nonlocal res
            if 0 <= i < len(grid) and 0 <= j < len(grid[0]) and grid[i][j] == 1:
                grid[i][j] = 0
                count = 1
                for x, y in directions:
                    newi, newj = x + i, y + j
                    count += dfs(newi, newj)
                res = max(res, count)
                return count
            return 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    dfs_count = dfs(i, j)
                    res = max(res, dfs_count)

        return res
 
        
