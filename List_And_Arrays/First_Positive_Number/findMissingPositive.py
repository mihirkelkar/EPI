def missingPositive(array):
  neg_ptr = 0
  for ii in range(0, len(array)):
    if array[ii] < 0:
      array[neg_ptr], array[ii] = array[ii], array[neg_ptr]
      neg_ptr += 1
  
  for ii in range(neg_ptr + 1, len(array)):
    if array[ii] < len(array) - 1:
      array[array[ii]] *= -1
    
  for ii in range(0, len(array)):
    if array[ii] > 0:
      return ii

print missingPositive([3, 4, -1, 1])
