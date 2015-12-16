class Node(object):
  """
  Lets add the size attribute to the node class where
  size is the number of descendant nodes that a goven node has
  So, if the left child has k - 1, then the root is the kth
  if the left child has less more than k - 1 nodes, then the kth node in the
  left subtree is the node, otherwise if left child has  less than k - 1 nodes 
  say l nodes, then k - l - 1 node in the right subtree is the node you want.
  """
  def __init__(self, value):
    self.left = None
    self.right = None
    self.value = value
    self.size = 0


def kthInorder(root, value):
  left_size = root.left.size if root.left is not None else 0
  right_size = root.right.size if root.right is not None else 0
  if left_size == value - 1:
    return root
  elif left_size > value - 1:
    return kthInorder(root.left, value)
  elif left_size < value - 1:
    if root.right != None:
      return kthInorder(root.right, value - left_size - 1)
  return False
        

def main():
      
