class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

def preOrderNext(node):
  if node.left != None:
    return node.left
  elif node.right != None:
    return node.right
  if node.parent == None:
    return None
  else:
    while node.parent != None:
      if node == node.parent.left:
        node = node.parent
        if node.right != None:
          return node.right
        else:
          node = node.parent
      
      elif node == node.parent.right:
        node = node.parent
    return None


"""

     1
    /  \
   2    5
    \
     3
    /
   4

We will check for 4 and 2, 5
"""
one =  Node(1)
one.left = Node(2)
one.left.parent = one
one.left.right = Node(3)
one.left.right.parent = one.left
one.left.right.left = Node(4)
one.left.right.left.parent = one.left.right
one.right = Node(5)
one.right.parent = one

print preOrderNext(one.left.right.left).value
print preOrderNext(one.left).value
print preOrderNext(one.right)
