def countMinSteps(target_array):
  result = 0
  zero_count = 0
  while zero_count < len(target_array):
    zero_count = 0
    target_array, temp = action(target_array) 
    print target_array, zero_count
    print "-----------------------"
    result += temp   
    for ii in target_array:
      if ii == 0:
        zero_count += 1
  return result

def AllEven(target_array):
  for ii in target_array:
    if ii % 2 != 0:
      return False
  return True

def action(array):
  if AllEven(array):
    return [ii / 2 for ii in array], 1
  else:
    result = 0
    for ii in range(0, len(array)):
      if array[ii] % 2 != 0:
        array[ii] -= 1
        result += 1
    return array, result

print countMinSteps([2, 3])
