# Leetcode - 129
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def dfs(node, val):
            nonlocal ans
            if not node:
                return
            val = val*10+node.val
            if not node.left and not node.right:
                ans+=val
                return
            dfs(node.left,val)
            dfs(node.right,val)
        if not root:
            return 0
        dfs(root,0)
        return ans 
