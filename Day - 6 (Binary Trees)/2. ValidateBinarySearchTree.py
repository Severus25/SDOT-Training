# Leetcode - 98
class Solution(object):
    def isValidBST(self, root, maximum = float('-inf'), minimum = float('inf')):
        if not root: return True
        if not maximum < root.val < minimum: return False
        return self.isValidBST(root.left, maximum, root.val) and self.isValidBST(root.right, root.val, minimum)
