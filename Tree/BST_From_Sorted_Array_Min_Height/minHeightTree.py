class Node(object):
  def __init__(self, value):
    self.value = value
    self.left  = None
    self.right = None
  



def minHeightTree(array):
  if len(array) == 0:
    return None
  else:
    mid = (0 + len(array)) / 2
    newNode = Node(array[mid])
    newNode.left = minHeightTree(array[:mid])
    newNode.right = minHeightTree(array[mid+1:])
    return newNode


temp = minHeightTree([1, 2, 3, 4, 5, 6, 7, 8])
print temp.value
print temp.left.value
print temp.left.left.value
print temp.left.right.value
print temp.right.value
