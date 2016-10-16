Given an array of integers, find the number that repeats the most in this array. Do so in O(n) time and O(1) space. 
The numbers in the array will be from 0 to k - 1 where k is the length of the array
Solution: 

Iterate through the array

and for every element i update arr[arr[i] % k] by k

index of the max element in the new array is the most repeating number in the old array
