class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        r1 = [0] * (len(grid[0])+2)
        r2 = [0] * (len(grid[0])+2)

        for i in range(len(r1)-2, 0, -1):
            r1[i] = grid[0][i-1] + r1[i+1]

        for i in range(1, len(r2)-1):
            r2[i] = grid[1][i-1] + r2[i-1]

        res = [] 

        for i in range(2, len(r1)):
            temp = max(r1[i], r2[i-2])
            res.append(temp)
        
        return min(res)

