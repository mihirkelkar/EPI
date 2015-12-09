Checked code looks okay. 
def reverseAlternate(llist):
  curr = llist.head
  listlen = 0
  while curr != None:
    listlen += 1
    curr = curr.next
  curnode = llist.head
  prev = None
  temp = curnode.next
  remNodes = listlen
  while True:
    if remNodes >= k:
      num = k
      firstNode = curnode
      while num > 0:
        temp = curnode.next
        curnode.next = prev
        prev = curnode
        curnode = temp
        remNodes -= 1
        num -= 1
      firstNode.next = curnode
      #This will fire only for the first inversion
      if remNodes == listlen - k:
        llist.head = prev
      if remNodes != 0:
        num = k
        while curnode != None and num > 0:
          prev = curnode
          curnode = curnode.next
          remNodes -= 1
        if num > 0:
          self.tail = prev
      else:
        self.tail = firstNode  
    break   
    
