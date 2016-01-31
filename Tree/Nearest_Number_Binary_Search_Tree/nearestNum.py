class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
  
class BinarySearchTree(object):
  def __init__(self):
    self.root = None
    self.nearLess = None
    self.nearMore = None

  def addNode(self, value, root=None):
    root = self.root if root is None else root
    if root == None:
      self.root = Node(value)
    else:
      if value <= root.value:
        if root.left == None:
          root.left = Node(value)
        else:
          self.addNode(value, root.left)
      else:
        if root.right == None:
          root.right = Node(value)
        else:
          self.addNode(value, root.right)

  def findNearestLeft(self, value, root=None):
    root = self.root if root is None else root
    if root == None:
      return None
    else:
      if value == root.value:
        self.nearLess = value
      elif value < root.value:
        if root.left != None:
          self.findNearestLeft(value, root.left)
        else:
          return None
      elif value > root.value:  
        if root.right != None:
          self.findNearestLeft(value, root.right)
        else:
          if self.nearLess != None:
            if root.value >= self.nearLess:
              self.nearLess = root.value
          else:
            self.nearLess = root.value 

  def findNearestRight(self, value, root=None):
    root = self.root if root is None else root
    if root == None:
      return None
    else:
      if value == root.value:
        self.nearMore = value
      elif value > root.value:
        if root.right != None:
          self.findNearestRight(value, root.right)
        else:
          return None
      elif value < root.value:
        if root.left != None:
          self.findNearestRight(value, root.left)
        else:
          if self.nearMore != None:
            if root.value <= self.nearMore:
              self.nearMore = root.value
          else:
            self.nearMore = root.value

def main():
  tree = BinarySearchTree()
  tree.addNode(10)
  tree.addNode(9)
  tree.addNode(11)
  tree.addNode(9.5)
  tree.addNode(8.5)
  tree.addNode(10.5)
  tree.addNode(11.5)
  print tree.root.left.left.value
  print tree.root.right.right.value
  tree.findNearestLeft(8.75)
  print tree.nearLess
  tree.findNearestRight(10.5)
  print tree.nearMore

if __name__ == "__main__":
  main()
