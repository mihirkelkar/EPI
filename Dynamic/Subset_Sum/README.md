Given an array of integers, find if there is a set that can sum up to a given value K. If such a set exists, return True. 


The idea is if the set is {1, 3, 6, 5} , and the number is 9, then retutn True

. 

Make a matrix like

           0  1  2  3  4
       0   T  F  F  F  F

       1   T
 
       3   T
  
       6   T

       5   T


The X is the target sum, the y is elements. The target sum 0 is always possible. Hence the column is all T
We can't make a target sum of 1 - 4 with 0. So the rest are false

can you make a target sum of 1 with 0 and 1. 
Lets find out. can we make a sum of 1 with 0?
     = mat[element - 1][target_sum] or mat[element - 1][target_sum - element]
  if target_sum - 1 is element then just copy the first val
