Suppose we could access yesterday's stock prices as a list, where:
 
1) The indcies are the time in minutes past trade opening time. 


Find the best profit that could have been made by one purchase and 1 sale of stock. 

Begin from the reverse, keep track of the max and min element found so far. 

If we find a new max, we reset the min to be equal to the max.
At the end. return max and min

