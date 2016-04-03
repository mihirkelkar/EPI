def equilibIndex(array):
  total = sum(array)
  cur_sum = array[0]
  for ii in range(1, len(array)):
    right_sum = cur_sum
    cur_sum += array[ii]
    left_sum = total - cur_sum
    if right_sum == left_sum:
      print ii
   
  
equilibIndex([-7, 1, 5, 2, -4, 3, 0]) 

    
