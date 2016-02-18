class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def lca(root, a, b):
  if root == None:
    return None
  
  if root == a or root == b:
    return root

  lca_l = lca(root.left, a, b)
  lca_r = lca(root.right, a, b)
  
  if lca_l != None and lca_r != None:
    return root
  
  if lca_l != None:
    return lca_l
  
  return lca_r


one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.left = two
one.right = three
two.left = four
two.right = five

print lca(one, four, five).value
