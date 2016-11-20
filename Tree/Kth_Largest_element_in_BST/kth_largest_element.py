class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


class Tree(object):
  def __init__(self):
    self.root = None

  def addNode(self, value, root = None)
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
  

def reverseInorder(root, k, count=0):
  if root is None:
    return count
  else:
    if root.right != None:
      count = reverseInorder(root.right, k, count)
    count += 1
    if count == k:
      print "The kth higest element in the tree is %d" % root.value
    if root.left != None:
      count = reverseInorder(root.left, k, count)

