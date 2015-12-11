Design an efficient algorithm for computing the LCA of nodes a and b in a binary tree in which nodes do not have a parent pointer. 

Lets begin from the root node. 
If the root node is a or b, then that is the lowest common ancestor. 

If not. 
Lets look at the left subtree : if the left subtree has both nodes, then the 
left child of the root is the lowest common ancestor. 

Same goes for the right child. 

If both nodes are in different subtree, then the root is the lowest common ancestor. 
