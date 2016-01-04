Search an array of sorted distinct integers for a[i] = i.

This can be solved using the binary search approach. 
Start with th mid. if a[m]-m < 0 then low = m + 1
if A[m] - m  > 0 then then high = mid - 1
