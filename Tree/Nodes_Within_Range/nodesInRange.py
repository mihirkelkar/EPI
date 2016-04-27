class Node(object):
  def __init__(self, value):
    self.value=value
    self.left=None
    self.right = None
 

def findCount(node, min, max):
  if node == None:
    return 0
  if node.value >= min and node.value <= max:
    return 1 + findCount(node.left, min, max) + findCount(node.right, min, max)
  elif node.value < min:
    return findCount(node.right, min, max)
  elif node.value > max:
    return findCount(node.left, min, max)
  
