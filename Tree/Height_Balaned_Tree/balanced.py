import math

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def checkBalanced(root):
  if root == None:
    return 0
  else:
    left_h = checkBalanced(root.left)
    right_h = checkBalanced(root.right)
    if left_h == -1 or right_h == -1:
      return -1
    if math.fabs(left_h - right_h) > 1:
      return -1
    return left_h + right_h + 1


def checkBalancedWrap(root):
  temp = checkBalanced(root)
  if temp == -1:
    return False
  return True 


"""
         1
    2        3
  4       6   7
5 


"""
one  = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left = two
one.right = three
two.left = four
four.left = five
three.left = six
three.right = seven

print checkBalancedWrap(one)
