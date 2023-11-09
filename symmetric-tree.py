class Solution:
    def isMirror(self, root1, root2):
            if root1 is None and root2 is None:
                return True
            if root1 is None or root2 is None:
                return False
            return (root1.val == root2.val) and self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
            
        return self.isMirror(root.left, root.right)
