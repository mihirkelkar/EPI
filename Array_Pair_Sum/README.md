Given an integer array. Output all pairs of numbers that sum up to a given 
number k

A naive way to do this would be to finish comparisons, but that would have a time complexity of O(n^2)


Another solution would be to sort the array and then do binary searches for 
the k - number. Thus this would have a timecomplexity of O(nLogn) required for the sort. 

Another solution would be to store all the numbers in a hash map in one pass. 
In the other pass. For each number , you check if k-number is present in the hash. But this is O(n) in time as well as space. 
