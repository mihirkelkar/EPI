class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNode(self, values):
    for value in values:
      if self.head == None:
        self.head = Node(value)
	self.tail = self.head
      else:
	self.tail.next = Node(value)
	self.tail = self.tail.next
    self.tail.next = self.head

def findMedianValue(linlist, node):
  smallest_val_node = node
  cur_node = node.next
  while cur_node != node:
    if cur_node.value < smallest_val_node.value:
      smallest_val_node = cur_node
    cur_node = cur_node.next
  head_node = smallest_val_node
  fast_ptr = head_node
  slow_ptr = head_node
  iter = 0
  while True:
    fast_ptr = fast_ptr.next.next
    prev_ptr = slow_ptr
    slow_ptr = slow_ptr.next
    if fast_ptr == head_node or fast_ptr.next == head_node:
      break
    iter += 1

  if fast_ptr == head_node:
    
    return float(slow_ptr.value + prev_ptr.value) / 2.0
  else: 
    return slow_ptr.value

def main():
  linkedlist = LinkedList()
  linkedlist.addNode([0, 1, 2, 3, 4])
  print findMedianValue(linkedlist, linkedlist.head.next)
  
if __name__ == "__main__":
  main()
