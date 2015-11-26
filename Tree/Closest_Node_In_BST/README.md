Given a binary search tree and a value k, please find a node in the binary search tree whose value is closest to k. 


Lets look at this logically. We need to keep track of the closest value in 
a variable. 

If the given number is less than the value of the node, we can bring the node value closer to the given value by moving to the right of the node and calculating the differece. 

If its greater than the given value, we can bring them close by moving to the left of the node and calculating the difference. 
