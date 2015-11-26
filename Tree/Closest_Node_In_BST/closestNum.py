class Node(object):

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None



class BTree(object):

  def __init__(self):
    self.root = None
 
  def addNode(self, value, root=None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    if value <= root.value:
      if root.left != None:
        self.addNode(value, root.left)
      else:
        root.left = Node(value)
    elif value > root.value:
      if root.right != None:
        self.addNode(value, root.right)
      else:
        root.right = Node(value)
  
  def findClosest(self, value):
    cur_node = self.root
    abs_diff = float("inf")
    while cur_node != null:
      if math.abs(cur_node.value - value) < abs_diff:
        abs_diff = math.abs(cur_node.value - value)
      if value == cur_node.value:
        reutrn cur_node.value
      elif value < cur_node.value:
          cur_node = cur_node.left
      elif value > cur_node.value
          cur_node = cur_node.right   
    return abs_diff  
