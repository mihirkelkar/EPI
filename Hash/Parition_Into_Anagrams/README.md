Given an array of strings, sort them such that the anagrams appear together. 

Example : 
Input: elvis, silent, debitcard, lives, listen, badcredit
Output: elvis, lives, silent, listen, debitcard, badcredit

Iterate through the list and sort string. 
Use the sorted strings as key in a hash map and its unsorted version as a value.If the key doesnt exist add it and then add the unsorted version as value

Thus , we can collect sorted and unsorted version together into a single key
and then print anagrams together. 

The total time complexity here in nmlogm. 
