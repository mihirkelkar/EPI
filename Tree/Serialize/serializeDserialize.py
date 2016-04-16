class Node(object):
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

def serialize(node):
  new_array = list()
  tr_array = [node]
  while tr_array:
    new_node = tr_array.pop(0)
    if new_node != None:
      left_node = new_node.left
      right_node = new_node.right
      tr_array.append(left_node)
      tr_array.append(right_node)
    new_array.append(new_node)


def deserialize(array):
  start = 0
  head_node = None
  index = ((len(array) - 1) - 2) / 2
  while start <= index:
    temp = Node(array[start])
    if start == 0:
      head_node = temp
    temp.left = Node(array[2*start + 1])
    temp.right =Node(array[2*start + 2])
    start += 1
  return head_node    
