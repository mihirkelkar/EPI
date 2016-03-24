class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

def removeDuplicates(node):
  back_node = Node(None)
  back_node.next = node
  middle_node = node
  front_node = middle_node.next
  flag = 0
  headnew = back_node 
  while node != None:
    if middle_node.value == front_node.value:
      flag = 1
      front_node = front_node.next
    else:
      if flag:
        middle_node = front_node
        front_node = front_node.next
        back_node.next = middle_node
       flag = 0
     else:
       back_node = back_node.next
       middle_node = middle_node.next
       front_node = front_node.next
  if flag:
    back_node.next = None
  return head_new.next
