class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None


def leftBoundary(node):
  left_path = list()
  while node != None:
    left_path.append(node.value)
    if node.left != None:
      node = node.left
    else:
        node = node.right
  return left_path

def rightBoundary(node):
  right_path = list()
  while node != None:
    right_path.append(node.value)
    if node.right != None:
      node = node.right
    else:
      node = node.left
  return right_path[::-1][:-1]

def midRiff(node, path):
  if node == None:
    return None
  leftval = midRiff(node.left, path)
  rightval = midRiff(node.right, path)
  if leftval == None and rightval == None:
    path.append(node.value)
  else:
    path = leftval
    if rightval != None:
      path = rightval
  return path
  

def main():
  eight = Node(8)
  three = Node(3)
  ten = Node(10)
  one = Node(1)
  six = Node(6)
  four = Node(4)
  seven  = Node(7)
  fteen = Node(14)
  tteen = Node(13)
  eight.left = three
  eight.right = ten
  ten.right = fteen
  fteen.left = tteen
  three.left = one
  three.right = six
  six.left = four
  six.right = seven
  temp = list()
  temp = leftBoundary(eight)
  temp += midRiff(eight, [])[1:-1]
  temp += rightBoundary(eight)
  print temp
if __name__ == "__main__":
  main()
