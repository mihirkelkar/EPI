class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None

def linked_list_palindrome(head):
  new_stack = list()
  if head == None:
    return True
  slow = head
  fast = head
  #1 2 3 3 2 1
  #1 2 3 2 1
  while fast != None and fast.next != None:
    new_stack.append(slow.value)
    fast = fast.next.next
    slow = slow.next
  #Odd length linked list
  if fast != None:
    new_stack.append(slow.value)
  while slow != None:
    if slow.value != new_stack.pop(-1):
      return False
    slow = slow.next

  if new_stack:
    return False
  return True

head = Node(1)
head.next = Node(2)

print linked_list_palindrome(head)

head = Node(1)
head.next = Node(2)
head.next.next = Node(3)
head.next.next.next = Node(2)
head.next.next.next.next = Node(1)

print linked_list_palindrome(head)
