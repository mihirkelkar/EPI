class Node(object):
  def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None


def arrayToBST(array):
  if len(array) == 0:
    return None
  else:
    middle = len(array) / 2
    root = Node(array[middle])
    root.left = arrayToBST(array[:middle])
    root.right = arrayToBST(array[middle+1:])
    return root

def main():
  array = [1, 2, 3, 4]
  root = arrayToBST(array)
  print root.left.left.value
  print root.right.value

if __name__ == "__main__":
  main() 
