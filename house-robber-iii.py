# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int: 
        memo = {}

        def dp(root):
            if root in memo:
                return memo[root] 
            if not root:
                return 0
            
            res = root.val
            if root not in memo:
                if root.left:
                    res += dp(root.left.left)
                if root.left:
                    res += dp(root.left.right)
                if root.right:
                    res += dp(root.right.left)
                if root.right:
                    res += dp(root.right.right)

                memo[root] = max(res, dp(root.left)+dp(root.right)) 
            return memo[root]

        return dp(root) 
