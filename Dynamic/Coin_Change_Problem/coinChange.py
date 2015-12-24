def coinChange(array, number):
  array = [0 for ii in range(0,number+1)]
  array[0] = 1
  
  for ii in range(0, len(array)):
    for jj in range(array[ii], number+1):
      array[jj] += array[jj-array[ii]]

  return array[number]

print coinChange([1, 2, 3] , 4)
