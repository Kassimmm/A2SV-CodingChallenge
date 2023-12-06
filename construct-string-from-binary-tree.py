class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        arr = ""

        def preorder(node):
            nonlocal arr
            if not node:
                return ""
            arr += str(node.val)
            if not node.left and node.right:
                arr += "()"
                arr += "(" 
                preorder(node.right) 
                arr += ")"
            elif node.left and not node.right:
                arr += "(" 
                preorder(node.left)
                arr += ")"
            elif node.left and node.right:
                arr += "(" 
                preorder(node.left)
                arr += ")"
                arr += "(" 
                preorder(node.right) 
                arr += ")"

        preorder(root)
        return arr
