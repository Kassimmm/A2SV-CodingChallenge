class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        queue = deque([((0, 0), 1)])
        visited = set((0, 0))
        res = float("inf")

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col and grid[r][c] == 0 and (r, c) not in visited

        if grid[0][0] == 1:
            return -1
        
        while queue:
            (r,c), length = queue.popleft()

            if r == row - 1 and c == col - 1:
                res = min(length, res)


            for x, y in directions:
                newr, newc = r + x, c + y

                if inbound(newr, newc):
                    queue.append(((newr, newc), length+1))
                    visited.add((newr, newc))

        return -1 if res == float("inf") else res 
