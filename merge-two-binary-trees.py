class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        res = TreeNode(root1.val + root2.val)
        res.left = self.mergeTrees(root1.left, root2.left)
        res.right = self.mergeTrees(root1.right, root2.right)
        return res
