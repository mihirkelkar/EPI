Check if removing an edge can divide a Binary Tree in two halves
Given a Binary Tree, find if there exist edge whose removal creates two trees of equal size.

Examples:

Input : root of following tree
           5
         /   \
       1      6    
      /      /  \
     3      7    4
Output : true
Removing edge 5-6 creates two trees of equal size


Input : root of following tree
           5
         /   \
       1      6    
            /  \
           7    4
         /  \    \
        3    2    8
Output : false
There is no edge whose removal creates two trees
of equal size.


Find the total number of nodes in the tree

Then while moving up in a bottom up manner, 
for a node if
node + num in left tree + num in right tree = total - (node + left right)
then true
