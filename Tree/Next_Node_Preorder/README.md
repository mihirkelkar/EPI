Given a tree and a node, find the next node in pre-ordel traversal of the tree. 

Parent pointers are provided. 

The idea here is if your left child is not none return that
else return right child if its not none

else:
  if you are left child, return parent's right child unless right child / parent
is not none

  if you are right child, return parent's parent's right child if it / parent is
  not none
