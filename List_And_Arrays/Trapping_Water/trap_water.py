def trap_water(array):
  max_element = array.index(max(array))
  
  #then we now iterate theough the left half of the array till the max_element
  left = array[0]
  cur = 1
  sum = 0
  while cur < max_element:
    if array[cur] >= left:
      left = array[cur]
    else:
      sum += left - array[cur]
    cur += 1

  
  #Now lets iterate through the right side
  if max_element == len(array):
    return sum
  right = array[-1]
  cur = len(array) - 2
  while cur > max_element:
    if array[cur] >= right:
      right = array[cur]
    else:
      sum += right - array[cur]
    cur -= 1
  return sum

print trap_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
  
