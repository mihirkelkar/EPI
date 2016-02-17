 number is called as a Jumping Number if all adjacent digits in it differ by 1. The difference between ‘9’ and ‘0’ is not considered as 1.
All single digit numbers are considered as Jumping Numbers. For example 7, 8987 and 4343456 are Jumping numbers but 796 and 89098 are not.

Given a positive number x, print all Jumping Numbers smaller than or equal to x. The numbers can be printed in any order.


The trick is to begin with the number 0
 in a queue
  while the q is empty, 
    num = pop q
    if num % 10 == 0
      add num*10+(next num) i.e   if num is 20 then add 201 coz next num of 0 is 1
    if num % 10 == 9:
      then add num*10 + 'prev num'  eg if num is 89 add 898 
        
    for num % 10 != 0  and != 9
      add num*10 + next num and num%10 + prev num   
