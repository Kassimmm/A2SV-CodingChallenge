class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        def dfs(i,j):
            grid[i][j] = "0"
            for x,y in directions:
                newi, newj = x+i, y+j
                if 0 <= newi < len(grid) and 0 <= newj < len(grid[0]) and grid[newi][newj] == "1":
                    dfs(newi, newj)
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1" :
                    count += 1
                    dfs(i,j)
                    
        return count
