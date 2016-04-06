def smallestNumber(array):
  low = 0
  high = len(array) - 1
  while low <= high:
    medium = (low + high) / 2
    if low < array[low]:
      return low
    else:
      if medium < array[medium]:
        high = medium - 1 
      else:
        low = medium + 1

  
print smallestNumber([0, 1, 2, 3, 4, 5, 6, 7, 10])
