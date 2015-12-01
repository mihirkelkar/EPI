def checkLinkPal(newList):
  cur = newList.head
  stack = list()
  while cur != None:
    stack.push(cur.value)
    cur = cur.next
  cur = newList.head()
  while cur != None:
    if cur.value != newList.pop():
      return False
  print "Palindrome"
