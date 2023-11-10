class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        if not root.left and not root.right:
            return root.val == targetSum
        
        path1 = self.hasPathSum(root.left, targetSum - root.val) 
        path2 = self.hasPathSum(root.right, targetSum - root.val)

        return path1 or path2
