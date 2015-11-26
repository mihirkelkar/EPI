Given a string, find all permutations of a given string. 

The idea actually is pretty simple. For a string of length n. Find all possible permutations of string length n - 1 and add the letter at position n in all positions possible in those strings. 


so for RMI you would have I as the nth letter and RM and MR as the permutations of the n-1 letters. Now insert I into all possible positions for RM and MR would give us

IMR MIR MRI RMI RIM IRM. The complexity here is O(n!) but this is optimal because there are n! permuatations for a string of length n
