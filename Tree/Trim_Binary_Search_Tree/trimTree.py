class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
 

class binaryTree(object):
  def __init__(self):
    self.root = None

  def addValue(self, value, root=None):
    root = self.root if self.root is None else root
    if self.root == None:
      self.root = Node(value)
    if value <= root.value:
      if root.left == None:
        root.left = Node(value)
      else:
        self.addValue(value, root.left)
    elif value > root.value:
      if root.right == None:
        root.right = Node(value)
      else:
        self.addValue(value, root.right)

  
def trimTree(min_value, max_value, node):
  if node.value == None:
    return None
  else:
    node.left = trimTree(min_value, max_value, node.left)
    node.right = trimTree(min_value, max_value, node.right)
    if min_value <= node.value and node.value <= max_value:
      return node
    if node.value < min_value:
      return node.right
    if node.value > max_value:
      return node.left


    
