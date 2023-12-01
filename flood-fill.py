class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        target = image[sr][sc]

        def dfs(i, j):
            if 0 <= i < len(image) and 0 <= j < len(image[0]) and image[i][j] == target and (i, j) not in visited:
                visited.add((i, j))
                image[i][j] = newColor
                for x, y in directions:
                    newi, newj = i + x, j + y
                    dfs(newi, newj)

        dfs(sr, sc)
        return image
