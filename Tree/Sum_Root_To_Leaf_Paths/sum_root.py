class Node(object):
  def __init__(self, data):
    self.data = data 
    self.left = None
    self.right = None

def sumPath(root, sum=0):
  if root == None:
    return 0
  else:
    sum = sum * 10 + root.data
    if root.left == None and root.right == None:
      return sum
    return sumPath(root.left, sum) + sumPath(root.right, sum)

def main():
  a = Node(1)
  b = Node(2)
  c = Node(4)
  d = Node(5)
  a.left = b
  b.left = c
  b.right = d
  e = Node(3)
  f = Node(6)
  g = Node(7)
  a.right = e
  e.left = f
  e.right = g
  print sumPath(a)

if __name__ == "__main__":
  main()
  
