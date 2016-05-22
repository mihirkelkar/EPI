class Node(object):
  def __init__(self, value):
    self.value = value 
    self.left = None
    self.right = None

def swap(root):
  if root == None:
    return 
  #if left subtree exists and left child is even
  if root.left != None:
    root.left.value, root.value = root.value, root.left.value
    swap(root.left)
  #else if right subtree exists and right child is even 
  elif root.right != None:
    root.right.value, root.value = root.value, root.right.value
    swap(root.right)

def sinkOddNodes(root):
  if root == None:
    return 
  else:
    sinkOddNodes(root.left)
    sinkOddNodes(root.right)
    if root.value % 2 != 0:
      swap(root)           





