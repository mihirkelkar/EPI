class Node(object):
  def __init__(self, value):
    self.value = value 
    self.left = None
    self.right = None

paths = list()

def path_sum(node, target,path, total = 0):
  global paths
  if node == None:
    return
  total += node.value
  if total   > target:
    return 
  else:
    if (total  == target) and (node.left==None and node.right==None):
       paths.append(path + [node.value])
    else:
      path_sum(node.left, target,path + [node.value],total)
      path_sum(node.right, target,path + [node.value],total)


def main():
  global paths
  five = Node(5)
  four = Node(4)
  five.left = four
  eight = Node(8)
  five.right = eight
  four.left = Node(11)
  four.left.left = Node(7)
  four.left.right = Node(2)
  eight.left = Node(13)
  eight.right = Node(4)
  eight.right.left = Node(5)
  eight.right.right = Node(1)

  path_sum(five, 22, [])
  print paths

main()
