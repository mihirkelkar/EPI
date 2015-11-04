class Node(object):
  def __init__(self, value):
    self.value = value
    self.next = None

class LinkedList(object):
  def __init__(self):
    self.head = None
    self.tail = None
  
  def addNode(self, value):
    if self.head == None:
      self.head = Node(value)
      self.tail = self.head
    else:
      self.tail.next = Node(value)
      self.tail = self.tail.next

def removeNode(lList, value):
  if self.head.value == value:
    current = self.head
    while current.value == value and current != None:
      current = current.next
    self.head = current
  newNode = self.head
  current = self.head
  while current.next != None and current:
    if current.next.value != value:
      current = current.next
    else:
      newNode = current
      while newNode.value == 5 and newNode != None:
        newNode = newNode.next
      current.next = newNode
      
