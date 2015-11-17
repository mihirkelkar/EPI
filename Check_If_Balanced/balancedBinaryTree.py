import sys
class Node(object):
  def __init__(self):
    self.value = value
    self.left = None
    self.right = None

def balancedTree(tree):
  if tree.left == None and tree.right == None:
    return 0
  else:
    left_height = balancedTree(tree.left) + 1
    right_height = balancedTree(tree.right) + 1
    if math.abs(left_height - right_height) > 1:
      print "Tree not balanced"
      sys.exit(1)
    else:
      max(left_height, right_height)
