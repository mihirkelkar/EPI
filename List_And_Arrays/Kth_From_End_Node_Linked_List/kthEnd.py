import random

class Node(object):
  def __init__(self, value):
    self.next = None
    self.value = value
 
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
  

def kthFromEnd(list, number):
  firptr = list.head
  secptr = list.head
  while number > 0:
    if secptr != None:
      secptr = secptr.next
    else:
      return "Linked list is not long enough"
    number -= 1

  while secptr.next != None:
    secptr = secptr.next
    firptr = firptr.next
  return firptr.next.value

def randomListGen(number):
  counter = number + random.randint(100, 100000)
  newList = LinkedList()
  while counter > 0:
    newList.addNode(random.randint(10000, 100000000))
    counter -= 1
  return newList
  
def main():
  print kthFromEnd(randomListGen(32), 32)

if __name__ == "__main__":
  main()
