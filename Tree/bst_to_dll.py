class Node(object):
  def __init__(self, value):
    self.value = value 
    self.left = None
    self.right = None


def fix_left_ptr(root):
  if root == None:
    return 
  else:
    fix_left_ptr(root.left)
    root.left = fix_left_ptr.prev
    fix_left_ptr.prev = prov
    fix_left_ptr(root.right)


def fix_right_ptr(root):
  while root != None and root.right != None:
    root = root.right:
  
  while root != None and root.left != None:
    prev = root
    root = root.left
    root.right = prev

  return root


