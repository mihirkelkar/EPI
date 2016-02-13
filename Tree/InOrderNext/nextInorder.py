class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None
    self.parent = None

def nextInorder(node):
  #If node has a right child, move to the left most child of the right child
  if node.right != None:
    node = node.right
    while node.left != None:
      node = node.left
    return node
  #If node does not have a right child
  elif node.right == None:
    if node.parent == None:
      return node
    else:
      if node == node.parent.left:
        return node.parent
      elif node == node.parent.right:
        while node == node.parent.right:
          node = node.parent
          if node.parent == None:
            return None
        return node.parent
  


"""
        1
     /     \
    2       3
   / \     /
  4   5   6
     / \   \
    7   8   12
   /
  9
 / \ 
10 11
  

  We will test for 11 which should yeild 7
  We will test for 3 which should yield 3 which should yeild none
  snd we will test for 8 which should say  1
"""
one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)
eight = Node(8)
nine = Node(9)
ten = Node(10)
ele = Node(11)
twe = Node(12)

one.left = two
one.right = three
two.parent = one
three.parent = one
three.left = six
six.parent = three
six.right = twe
twe.parent = six
two.left = four
two.right = five
four.parent = two
five.parent = two
five.left = seven
five.right = eight
seven.parent = five
eight.parent = five
seven.left = nine
nine.parent = seven
nine.left = ten
nine.right = ele
ten.parent = nine
ele.parent = nine

print nextInorder(ele).value
print nextInorder(three)
print nextInorder(eight).value
