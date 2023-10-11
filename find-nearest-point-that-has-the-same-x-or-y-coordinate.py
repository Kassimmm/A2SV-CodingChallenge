class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        valid_points = []
        min_distance = float('inf')
        min_index = -1

        for i, point in enumerate(points):
            px, py = point
            if px == x or py == y:
                distance = abs(px - x) + abs(py - y)
                if distance < min_distance:
                    min_distance = distance
                    min_index = i

        return min_index

"""
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        maha = {}
        ans, res = -1, float("inf")
        for i in range(len(points)):
            if points[i][0] == x or points[i][1] == y:
                maha[i] = abs(x - points[i][0]) + abs(y - points[i][1])
        
        for key, value in maha.items():
            if value >= 0 and value < res:
                ans = key
                res = value

        return ans
"""
