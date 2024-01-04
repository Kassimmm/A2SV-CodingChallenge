class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque()
        visited = set()

        queue.append(("0000", 0))
        visited.add("0000")

        while queue:
            pattern, path = queue.popleft()

            if pattern == target:
                return path
                
            if pattern in deadends:
                return -1

            for i in range(len(target)):
                temp1 = pattern[:i] + str((int(pattern[i])+1) % 10) + pattern[i+1:]
                temp2 = pattern[:i] + str((int(pattern[i])-1) % 10) + pattern[i+1:]


                if temp1 not in visited and temp1 not in deadends:
                    queue.append((temp1, path+1))
                    visited.add(temp1)
                
                if temp2 not in visited and temp2 not in deadends:
                    queue.append((temp2, path+1))
                    visited.add(temp2)
        return -1
