def llAlternate(llist):
  oddhdr = llist
  odd = oddhdr
  if odd == None or odd.next == None or odd.next.next == None:
    return None
  else:
    even = odd.next
    odd.next = odd.next.next
    odd = odd.next
    even.next = None
    while odd != None and odd.next != None:
      temp_even = odd.next
      new_odd = odd.next.next
      temp_even.next = even
      even = temp_even
      if new_odd == None:
        break
      else:
        odd.next = new_odd
        odd = odd.next
    odd.next = even
    while oddhdr != None:
      print oddhdr.value
      oddhdr = oddhdr.next 
 
class Node(object):
  def __init__(self, value):
    self.next = None
    self.value = value


def main():
  one = Node(1)
  two = Node(2)
  one.next = two
  thr = Node(3)
  two.next = thr
  four = Node(4) 
  thr.next  = four
  fiv = Node(5)
  four.next = fiv
  six = Node(6)
  fiv.next = six
  llAlternate(one)

main()   
