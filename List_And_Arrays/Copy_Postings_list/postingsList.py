def duplicateList(head):
  if head == None:
    return None
  else:
    current =  head
    while current != None:
      duplicate = Node(current.value)
      duplicate.next = current.next
      current.next = duplicate
      current = duplicate.next
    cur = head
    while cur != None:
      cur = cur.next
    return head  

def copyJumps(head):
  if head == None:
    return None
  else:
    current = head
    while current != None:
      if current.jump != None:
        current.next.jump = current.jump.next
      if current.next != None:
        current = current.next.next 
    return head

def separateList(head):
  if head == None:
    return None
  current = head.next
  headNode = current
  while current != None:
     if current.next != None:
       current.next = current.next.next
     else:
       current.next = None
     current = current.next
  return headNode

def copyPostings(head):
  head = duplicateList(head)
  head = copyJumps(head)
  return separateList(head)

class Node(object):
  def __init__(self, value):
    self.next = None
    self.jump = None
    self.value = value

def main():
  one = Node(1)
  two = Node(2)
  three = Node(3)
  four = Node(4)

  one.next = two
  two.next = three
  three.next = four
  
  one.jump = three
  three.jump = two
  temp = copyPostings(one)  
  print temp.jump.value

if __name__ == "__main__":
  main()
