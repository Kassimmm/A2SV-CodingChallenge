class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def fun(root, val):
            if not root:
                return TreeNode(val)
            
            if root.val > val:
                root.left = fun(root.left, val)
            if root.val < val:
                root.right = fun(root.right, val)
            return root
        return fun(root, val)
