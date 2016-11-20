class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class BSTree(object):
  def __init__(self):
    self.root = None
    
  def addNode(self, value, root=None):
    root = self.root if root is None else root
    if root is None:
      root = Node(value)
    else:
      if value <= root.value:
        if root.left is None:
          root.left = Node(value)
        else:
          self.addNode(value, root.left)
      else:
        if root.right is None:
          root.right = Node(value)
        else:
          self.addNode(value, root.right)
  
def reverseInorder(root, count=0):
  if root is not None:
    if root.right != None:
      count = reverseInorder(root.right, count)
    count += 1
    if count == 2:
      print "This is the root %s" root.value
    if root.left != None:
      count = reverseInorder(root.left, count)
    return count
        
