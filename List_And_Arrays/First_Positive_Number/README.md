Given an unsorted array, find the first missing positive integer. 

For example , [1, 2, 0] return 3
  [3, 4, -1, 1] return 2


Sol : 
  Move all negatives to the left, 

  Now look at the posisitve array
 if x is the number mark array[x] as negative
 now traverse array after its done again and return the index of the positive number in the array
