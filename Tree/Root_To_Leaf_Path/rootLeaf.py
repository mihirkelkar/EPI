class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def checkPath(valuecheck, root, sum=0):
  if sum + root.value == valuecheck:
    return True
  else:
    if root.left != None:
        retleft = checkPath(valuecheck, root.left, sum + root.value)
    if root.right != None:
      retright = checkPath(valuecheck, root.right, sum + root.value)
    return retleft or retright
    
def main():
  root = Node(1)
  root.left = Node(2)
  print checkPath(3, root)
  
if __name__ == "__main__":
  main()
