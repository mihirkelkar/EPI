class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def mirrorThis(node):
  if node == None:
    return None
  tempNode = mirrorThis(node.right)
  node.right = mirrorThis(node.left)
  node.left = tempNode
  return node

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)

one.left = three
one.right = two
two.left = five
two.right = four

print mirrorThis(one).left.right.value
