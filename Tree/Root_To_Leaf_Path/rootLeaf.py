class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def checkPath(valuecheck, root, sum=0):
  if root == None:
    return False
  if root.value + sum == valuecheck:
    return True
  retLeft = checkPath(valuecheck, root.left, sum + root.value)
  retRight = checkPath(valuecheck, root.right, sum + root.value)
  return retLeft or retRight


def main():
  root = Node(1)
  root.left = Node(2)
  print checkPath(3, root)
  
if __name__ == "__main__":
  main()
