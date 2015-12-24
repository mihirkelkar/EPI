Given a value N, if we want to make change for N cents, and we have an infinite supply of coins of each of a set s = {s1, s2, s3} values coins. In how many
ways can we make change. The order of coins doesnt not matter. 

For example, for N=4 and s= {1, 2, 3}. We could do 1, 1, 1, 1 and 1, 1, 2 and 2, 2 and 1, 3. So, the output should be 4. 
 

initialize an array of size n+1. Mark the first element as 1. 

Iterate through the coins and update the index greater than or equal to the value of the picked coin. 
