class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BTree(object):
  def __init__(self):
    self.root = None

def reverseBTree(node):
  node.right, node.left = node.left, node.right
  if node.left != None:
    reverseBTree(node.left)
  if node.right != None:
    reverseBTree(node.right)
  return node

def main():
  newTree = BTree()
  newTree.root = Node('a')
  newTree.root.left = Node('b')
  newTree.root.left.left = Node('d')
  newTree.root.left.right = Node('e')
  newTree.root.right = Node('c')
  newTree.root.right.left = Node('f')
  newTree.root.right.right = Node('g')
  newTree.root = reverseBTree(newTree.root)
  print newTree.root.left.value

main()
