Given a sorted array of unknown length and a number to search for, return the index of the number in the array. Accessing an element out of bounds throws exception. If the number occurs multiple times, return the index of any occurence. If it isn't present, return -1. 

Solutions: 
1)You could do a linear search that could take linear time. 

2)By standard binary search, will not work since the size of the given array is an unkown here. 
So, we essentially move ahead in exponents of 2. We go to 2, if the number is larger than the number we're looking for, we do a complete binary search. Else we go to 4, then if unsuccesful, onto 8 and so on. 
