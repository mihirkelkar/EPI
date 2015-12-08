class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None

  def addNode(self, value):
    if self.tail == None:
      self.tail = Node(value)
      self.head = self.tail
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next
  
  def printList(self):
    curr = self.head
    while curr != None:
      print curr.value
      curr = curr.next

def reverseList(llist):
  curr = llist.head
  prev = None
  while curr != None:
    temp = curr.next
    curr.next = prev
    prev = curr
    if temp == None:
      break
    curr = temp
  llist.head = curr
  return llist

temp = LinkedList()
temp.addNode(1)
temp.addNode(2)
temp.printList()
print "------"
reverseList(temp).printList()
