Given a list of ints, find the highest product you can get from three of the 
integers. 

The answer is to keep track of the two minimal elements and three maximal elements, the answer is min1 * min2 * max1 or max1 * max2 * max3

this results in a O(n) runtime. 
