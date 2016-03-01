class Node(object):
  def __init__(self, value):
    self.value = value
    self.prev = None
    self.next = None

class Stack(object):
  def __init__(self):
    self.head = None
    self.tail = None
    self.capacity = 0
    self.middle = None

  def push(self, value):
    if self.capacity == 0:
      self.head = Node(value)
      self.capacity += 1
      self.tail = self.head
      self.middle = self.head
    else:
      self.tail.next = Node(value)
      self.tail.next.prev = self.tail
      self.tail = self.tail.next
      self.capacity += 1
      if self.capacity%2 == 1:
        self.middle = self.middle.next
  
  def pop(self):
    temp = None
    if self.capacity == 1:
      temp = self.head.value
      self.head = self.tail = self.middle = None
    elif self.capacity > 1:
      temp = self.tail.value
      self.tail = self.tail.prev
    self.capacity -= 1
    if self.capacity % 2 == 0:
      self.middle = self.middle.prev
    return temp   

  def findMiddle(self):
    return self.middle.value

  def deleteMiddle(self):
    if self.capacity >= 3:
      prev = self.middle.prev
      next = self.middle.next
      prev.next = next
      self.capacity -= 1
      if self.capacity % 2 == 0:
        self.middle = prev
      else:
        self.middle = next 
    else:
      if self.capacity == 1:
        self.head = None
      elif self.capacity == 2:
        self.head = self.tail
        self.tail.prev = None
        self.middle = self.tail
      self.capacity -= 1 

  def printS(self):
    cur = self.head
    while cur != None:
      print cur.value
      cur = cur.next

temp = Stack()
temp.push(1)
temp.push(2)  
temp.pop()
temp.push(3)
temp.push(2)
temp.deleteMiddle()
temp.deleteMiddle()
temp.printS()

