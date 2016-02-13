Check if a given linked list is a palindrome

You start with two pointers, one fast the other slow. 

While the fast pointer hasn't reached the end, you push everything from the slow pointer onto a stack. 

We should definetely be considering even and odd number of nodes in the linked list

When the fast pointer reaches the end, you increment the slow pointer and pop from the stack to compare. If they keep matching up, you're fine. 

1 2 2 3 3 2 2 1

1 2 3 2 1
