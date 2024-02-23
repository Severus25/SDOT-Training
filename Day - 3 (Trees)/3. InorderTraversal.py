#Leetcode - 94
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        self.printInorder(root, answer)
        return answer
    
    def printInorder(self, node, answer):
        if node is None:
            return

        self.printInorder(node.left, answer)

        answer.append(node.val)

        self.printInorder(node.right, answer)
        
        
