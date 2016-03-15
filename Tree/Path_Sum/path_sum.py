class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def pathSum(root, count, sum):
  if root == None:
    return False
  else:
    count += root.value
    if count == sum:
      return True
    elif count < sum:
      left_h = pathSum(root.left, count, sum)
      right_h = pathSum(root.right, count, sum)
      return left_h or right_h
    return False


root = Node(5)
root.left = Node(4)
root.left.left = Node(11)
root.left.left.left = Node(7)
root.left.left.right = Node(2)
root.right = Node(8)
root.right.left = Node(13)
root.right.right = Node(4)
root.right.right.right = Node(1)
print pathSum(root, 0, 22)
