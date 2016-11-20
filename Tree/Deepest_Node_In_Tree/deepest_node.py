class Node(object):
  def __init__(self, value)
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

find_deepest_node(tree):
  root_node = tree.root
  if root_node == None:
    print "Your tree looks empty dude"
  this_level = [root_node]
  next_level = list()
  while this_level:
    cur_node = this_level.pop(0)
    if cur_node.left is not None:
      next_level.append(cur_node.left)
    elif cur_node.right is not None:
      next_level.append(cur_node.right)
    if len(this_level) == 0:
      this_level = next_level
      next_level = list()
  print "The deepest node in this case is {node}".format(node = cur_node.value)

