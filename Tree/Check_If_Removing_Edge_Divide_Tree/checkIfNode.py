class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def checkRemoveNode(root, total_count):
  if root == None:
    return 0
  left_count = checkRemoveNode(root.left, total_count)
  right_count = checkRemoveNode(root.right, total_count)
  if type(left_count) is not int or type(right_count) is not int:
    return True
  else:
    so_far = 1 + left_count + right_count
    if so_far == total_count - so_far:
      return True
    return so_far
  

def total_countFunc(node):
  if node == None:
    return 0
  return 1 + total_countFunc(node.left) + total_countFunc(node.right)


def checkRemoveNodeHelper(node):
  total_count = total_countFunc(node)
  if checkRemoveNode(node, total_count) == True:
    return True
  return False


def main():
  five = Node(5)
  one = Node(1)
  three = Node(3)
  six = Node(6)
  seven = Node(7)
  four = Node(4)
  five.left = one
  five.right = six
  one.left = three
  six.left = seven
  six.right = four
  print checkRemoveNodeHelper(five)
  
  node = Node(5)
  node.left = Node(1)
  node.right = Node(6)
  node.right.left = Node(7)
  node.right.right = Node(4)
  node.right.left.left = Node(3)
  node.right.left.right = Node(2)
  node.right.right.right = Node(8)
  print checkRemoveNodeHelper(node)

if __name__ == "__main__":
  main()
    
