 Count Derangements

A derangement is a permutation of n elements such that no element appears in its original place. For a derangement of {0, 1, 2, 3} is {2, 3, 1, 0}


For 1 elements, there are no possible de-rangements. 
For 2 elements , there is just the 1. 
For n numbers, 
each elements can be placed at n - 1 other locations. 
So essentially. for n it is n - 1 * (count(n - 1) + count(n - 2))
