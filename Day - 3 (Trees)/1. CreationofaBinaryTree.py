class Node:
  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None

class BinaryTree:
  idx = -1

@staticmethod
def build_tree(nodes):
  BinaryTree.idx += 1
  if nodes[BinaryTree.idx] == -1:
    return None
  new_node = Node(nodes[BinaryTree.idx])
  new_node.left = BinaryTree.build_tree(nodes)
  new_node.right = BinaryTree.build_tree(nodes)
  return new_node

if __name__ == "__main__":
  nodes = [1,2,4,-1,-1,5,-1,-1,3,-1,6,-1,-1]
  tree = BinaryTree()
  root = tree.build_tree(nodes)
  print(root.data)
