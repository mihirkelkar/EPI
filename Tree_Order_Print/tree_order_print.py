class Node(object):
  
  def __init__(self, value):
    self.right = None
    self.left = None
    self.value = value

class Tree(object):

  def __init__(self):
    self.root = None
  
  def addNode(self, value, root = None):
    root = self.root if root is None else root
    if root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left != None:
          self.addNode(value, root.left)
        else:
          root.left = Node(value)
      else:
        if root.right != None:
          self.addNode(value, root.right)
        else:
          root.right = Node(value)

  def tree_order(self):
    bfs_queue = [self.root]
    level_count = 1
    while bfs_queue:
      temp = bfs_queue.pop(0)
      print temp.value,
      level_count -= 1
      if temp.left != None:
        bfs_queue.append(temp.left)
      if temp.right != None:
        bfs_queue.append(temp.right)
      if level_count == 0:
        print "\n"  
        level_count = len(bfs_queue)
      
tree_one = Tree()
tree_one.addNode(2)
tree_one.addNode(1)
tree_one.addNode(3)
tree_one.addNode(0.8)
tree_one.addNode(1.1)
tree_one.addNode(2.5)
tree_one.addNode(3.2)
tree_one.tree_order()  
