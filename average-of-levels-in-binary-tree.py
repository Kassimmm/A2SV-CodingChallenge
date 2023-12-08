class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]: 
        queue = deque()
        queue.append(root)

        _average = []
        while queue:
            boundary = len(queue)
            _sum = 0

            for _ in range(boundary):
                temp = queue.popleft()
                _sum += temp.val

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            _average.append(_sum / boundary)
        return _average
        
