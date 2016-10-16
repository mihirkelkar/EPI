def max_repeat_number(array):
  k = len(array)
  for ii in range(0, len(array)):
    array[array[ii] % k] += k
  temp_max = -float("inf")
  index = 0
  for ii in range(0, len(array)):
    if array[ii] > temp_max:
      temp_max = array[ii]
      index = ii
  return index

print max_repeat_number([8, 2, 8, 2, 3, 8, 8, 9, 2, 3])    
