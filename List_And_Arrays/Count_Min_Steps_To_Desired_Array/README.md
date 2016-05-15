Consider an array with n elements and value of all the elements is zero. We can perform
following operations on the array

1. Incremental operations : Choose 1 element from the array and increment its value by 1
2. Doubling operation: Double the values of all the elements of the array. 

Solution: 

Take the target array, if all elements are event, then divide all elements by 2 and increment result by 1. 

Find all odd elements and reduce them by 1. For every reduction, increment the result by 1

Finally , we get all zeroes in target array. 


