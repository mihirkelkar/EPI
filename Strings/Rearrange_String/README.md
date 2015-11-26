Re-arrange characters in a string so that no character repeats twice next to 
each other. 

eg. aaabc changes to abaca. 
    aa - > No valid output
    aaaabc -> No valid output. 

This is actually an awesome questions that involves solving by the pegion hole principle. But, il spare the theoratical details. 

Lets get to the actual solution then. 

In a string of length n, if any character occurs more than (n + 1) / 2 times, 
this would be an invalid output. 

For all other cases, we parse the string from left to right and store the
characters and their frequencies in a hash table. Assuming that no character occurs more than (n+1) / 2 times, we start filling the characters in a n length array. 

Now, in this case, we begin with the most frequent character and fill it in the 0th, 2nd, 4th, 6th and so on index. When we encounter the end of the array, we roll back to the next unfilled index. This ensures that no character ever occurs next to each other. 
