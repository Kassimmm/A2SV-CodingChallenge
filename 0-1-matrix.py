class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = deque()

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = "#"

        while queue:
            i, j = queue.popleft()
            for x, y in directions:
                r,c = i+x, j+y
                if 0 <= r < len(mat) and 0 <= c < len(mat[0]) and mat[r][c] == "#":
                    mat[r][c] = mat[i][j] + 1
                    queue.append((r,c))

        return mat
