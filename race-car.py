class Solution:
    def racecar(self, target: int) -> int:
        queue = deque()
        visited = set()
        queue.append((0,1,0))
        visited.add((0,1))

        while queue:
            position, speed, count = queue.popleft() 

            if position == target:
                return count
            if (position + speed, speed * 2) not in visited:
                queue.append((position + speed, speed * 2, count+1))
                visited.add((position + speed, speed * 2))

            if speed > 0:
                if (position, -1) not in visited:
                    queue.append((position, -1, count+1))
                    visited.add((position, -1))
            else:
                if (position, 1) not in visited:
                    queue.append((position, 1, count+1))
                    visited.add((position, 1))
            

        return -1
