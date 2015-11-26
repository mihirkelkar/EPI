Q;Given a number whose digits are unique, find the enxt number that can be formed with those digits. 

Solution: If all the digits are in increasing order from the right to the left, then no larger number is possible. If not, begin from the number in the ten's place. If the number to rhe right <= current number. Move ti the right. Keep a track of the smallest number so far. When the number to the right > current_number. Then stop. swap current number with the smallest number so far. then go ahead and sort everything to the right of the current number
