class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def inorder(root, prev):
  if root == None:
    return None
  inorder(root.left, prev)
  root.left = prev
  prev = root
  inorder(root.right, prev)

def fixRights(root)
  while root.right != None and root != None:
    root = root.right
  while root != None and root.left != None:
    prev = root
    root = root.left
    root.right = prev
  return root

def treeDll(root):
  inorder(root, None)
  return fixRights(root)
