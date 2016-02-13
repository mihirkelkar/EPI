Given a node, find the lement whch will be next in an inorder traversal of a tree. 
If the node has a right child:
  If the node's right child has a left child .. and so on
If the node does not have a right child:
  If  the node does not have parent:
    return None
  is the node a left child of the parent
    return parent
  If node is right child of the parent
    move up until the node is left child of the parent and print node's parent
