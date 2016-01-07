Given an array that is almost sorted, where each numbers is at most k positions
away from its final place in the sorted array. Sort this array efficiently

Input: array and a number k. 

Solution: Use a min-heap and add k - elements to begin with. 

Then after the heap has k elements, every time you add an element, pop the top and heapify
