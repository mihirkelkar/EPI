arrange the numbers in an array in an alternate order. 
For example, if the array is [a1, a2, a3, a4, a5] arrange the array such that 
a1 <= a2 >= a3 <= a4 >= a5. 

The way to do that is pretty simple. This can be done in a linear time. 
Start iterating through the array from the first index.
Notice how odd indexes are greater than even indexes. 

So if its an odd index and its less than the previous index, you swap with the prev index. 
If its an even index and its greater than its previous index, you swap with the previous index. 
