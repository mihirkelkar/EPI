Given an array of integers, write a method to find indices m and n such that if you sorted elements m through n , the entire array would be sorted. 


The idea here is to find 
1) an increasing sequence in the beginning
2) an increasing sequence in the end
3) middle part. 
4)Now move back in the left subseq till you find an element smaller than the smallest in the middle
5) move back in the right subseq until you find an element larger then the largest in the middle
