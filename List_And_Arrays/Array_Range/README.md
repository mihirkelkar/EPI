Given an array of array range, return an optimized array by deleting sub arrays. 
NOTE: Array range (2, 6) represents (2, 3, 4, 5, 6)

INPUT : [(2, 6), (3, 5), (7, 21), (20, 21)]
OUTPUT: [(2, 6), (7, 21)]
REASON: (3, 5) is a sub array of (2, 6) and (20, 21) is a sub array of (7, 21)

The way to solve this is to sort the pairs according to their first element and then compare each one with the one before it. if first element of pair x is greater than pair x - 1 but smaller than the second element of x - 1, check if the second element of x is smaller than or equal to the second element of x - 1.If thats the case, pair x can be gobbled up. 

Also look for the case where the first element of x is equal to the first element of x - 1 and the second element of x is greater than the second element of x - 1. In that case, pair x - 1 has to go.   
