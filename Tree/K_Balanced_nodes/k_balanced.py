import math

class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None 
    self.right = None 


def kUnbalanced(node, k):
  if node == None:
    return 0
  else:
      nodes_left = kUnbalanced(node.left, k)
      if type(nodes_left) is not int:
        return nodes_left
      nodes_right = kUnbalanced(node.right, k)
      if type(nodes_right) is not int:
        return nodes_right
      if math.fabs(nodes_left - nodes_right) <= k:
        return nodes_left + nodes_right + 1
      else:
        return node

def main():
  a = Node(314)
  b = Node(6)
  c = Node(271)
  d = Node(28)
  e = Node(0)
  f = Node(561)
  g = Node(3)
  h = Node(17)
  i = Node(6)
  j = Node(2)
  k = Node(1)
  l = Node(401)
  m = Node(641)
  n = Node(257)
  o = Node(271)
  p = Node(28)
  a.left = b
  a.right = i
  b.left = c
  b.right = f
  c.left = d
  c.right = e
  f.right = g
  g.left = h
  i.left = j
  i.right = o
  j.right = k
  k.left = l
  k.right = n
  l.right = m
  o.right = p
  print kUnbalanced(a, 3).value


if __name__ == "__main__":
  main()
  
