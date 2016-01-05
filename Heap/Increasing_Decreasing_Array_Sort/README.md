Given an array whose elements are in increasing-decreasing order, sort them in the most efficient order

Input: 1, 5, 10, 15, 13, 11, 12, 14, 20, 18, 16, 17, 19, 30
       ----------><------><----------><------><-----------

Solution:
Split array into sorted increasing arrays. 
Merge using a min heap
