Given a range of numbers and a bianry search tree. Keep only those nodes that are between both the given values. Both values inclusive. 

The trick is to do a post order traversal  of the tree. 
If a node's value is less than the min, return its right sub tree
If a node's value is greater than the max, return its left subtree. 
If its within the range. return the node itself. 

