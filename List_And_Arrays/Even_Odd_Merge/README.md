Write a function that takes a singly linked list and re-orders the elements of L so that the new list represents even-odd(L). Your function should use O(1) additional storage. 

Eg. Input 1,2,3,4,5,6
    Output: 1,3,5,2,4,6

>Start with odd and even pointers
odd = head
even = head.next


