class Node(object):
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value

class Tree(object):
  def __init__(self):
    self.root = None

  def addNode(self, value, root = None):
    root = self.root if root is None else root
    if self.root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left == None:
          root.left = Node(value)
        else:
          self.addNode(value, root.left)
      elif value > root.value:
        if root.right == None:
          root.right = Node(value)
        else:
          self.addNode(value, root.right)

  def reverseTreePrint(self):
    bfs_queue = [self.root]
    final_queue = []
    currentLevel = 1
    tempNodeQueue = list()
    while bfs_queue:
      tempNode = bfs_queue.pop(0)
      if tempNode.left != None:
        bfs_queue.append(tempNode.left)
      if tempNode.right != None:
        bfs_queue.append(tempNode.right)
      tempNodeQueue.append(tempNode)
      currentLevel -= 1
      if currentLevel == 0:
        final_queue.append(tempNodeQueue)
        tempNodeQueue = list()
        currentLevel = len(bfs_queue)
    for ii in final_queue[::-1]:
      print " ".join([str(jj.value) for jj in ii])


tree = Tree()
tree.addNode(4)
tree.addNode(3)
tree.addNode(5)
tree.addNode(3.5)
tree.addNode(2)
tree.addNode(4.5)
tree.addNode(6)
tree.reverseTreePrint()
