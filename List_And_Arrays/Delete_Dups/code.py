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



def deleteDuplicate(node):
  if node == None:
    return None
  cur = node
  current = cur
  tracker = current.next
  while tracker != None:
    if current.value == tracker.value:
      tracker = tracker.next
      if tracker  == None:
        current.next = tracker
    else:
      current.next = tracker
      current = current.next
      tracker = current.next
  return cur


def main():
  ll = LinkedList()
  for ii in [1, 1, 1, 2, 2, 2, 3, 3]:
    ll.addNode(ii)
  cur = deleteDuplicate(ll.head)
  while cur != None:
    print cur.value
    cur = cur.next

main()
