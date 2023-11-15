class Solution:
    def __init__(self):
        self.arr = []

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def func(root):
            if not root:
                return
            if root.left:
                func(root.left)
            self.arr.append(root.val)
            if root.right:
                func(root.right)

        if not root:
            return 0

        func(root)
        return self.arr[k-1]
