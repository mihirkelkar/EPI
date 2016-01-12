def even_odd_merge(head):
  odd_ptr = head
  even_ptr = head.next
  
  first_odd_ptr = odd_ptr
  first_even_ptr = even_ptr
  
  while odd_ptr != None and even_ptr != None:
    if odd_ptr.next != None:
      odd_ptr.next = odd_ptr.next.next
      odd_ptr = odd_ptr.next
    if even_ptr.next != None:
      even_ptr.next = even_ptr.next.next
      even_ptr = even_ptr.next
 
  odd_ptr.next = first_even_ptr
  return first_odd_ptr

class Node(object):
  def __init__(self,value):
    self.value = value
    self.next = None


def main():
  one = Node(1)
  one.next = Node(2)
  one.next.next = Node(3)
  new_list_head = even_odd_merge(one)
  cur = new_list_head
  while cur != None:
    print cur.value
    cur = cur.next

if __name__ == "__main__":
  main()  
