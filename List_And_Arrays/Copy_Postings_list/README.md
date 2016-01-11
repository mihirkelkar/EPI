You are given a postings list, where each node in the linked list has 2 pointers, one pointing to the next node and other pointing to a random node in the list. Duplicate this list

Step 1: Create new nodes for evey nodes
For a given current node. 
Make a new node. 
Add it like 
  dup.next = current.next
  current.next = dup
  current = dup.next
  

Step 2: Update the jumper pointers for the duplicate nodes bu just copying them
for their previous nodes. 

Step 3 : separate the lists and retuen head
  
