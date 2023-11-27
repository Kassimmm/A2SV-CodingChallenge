class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: return 0
        res = 0
        path = []
        def helper(node):
            nonlocal res
            if not node:
                return
            if not node.children:
                path.append(node)
                res = max(res, len(path))
                path.pop()

            path.append(node)
            for i in node.children:
                helper(i)
            path.pop()
        helper(root)
        return res
