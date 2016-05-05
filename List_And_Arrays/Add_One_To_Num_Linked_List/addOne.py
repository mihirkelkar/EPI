class Node(object):
  def __init__(self, value):
    self.value = value 
    self.next = None


def addOne(value, node):
  if node != None:
    carry = addOne(value, node.next)
    carry += node.value
    node.value = carry % 10
    print node.value
    return carry / 10
  else:
    return value


temp = Node(1)
temp.next = Node(9)
temp.next.next = Node(9)
addOne(1, temp)


