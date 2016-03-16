def rangeLeftSearch(array, value, low, high):
  while low <= high:
    middle = (low + high) / 2
    if array[middle] == value:
      left = rangeLeftSearch(array, value, low , middle-1)
      if left == -1:
        return middle
      return left
    elif array[middle] < value:
      low = middle + 1
    elif array[middle] > value:
      high = middle - 1
  return -1

def rangeRightSearch(array, value, low, high):
  while low <= high:
    middle = (low + high) / 2
    if array[middle] == value:
      right = rangeRightSearch(array, value, middle + 1, high)
      if right == -1:
        return middle
      return right
    elif array[middle] < value:
      low = middle + 1
    elif array[middle] > value:
      high = middle - 1
  return -1

def rangeWrapper(array, value):
  left = rangeLeftSearch(array, value, 0, len(array) - 1)
  right = rangeRightSearch(array, value, 0, len(array) - 1)
  return (left, right)
 

print rangeWrapper([5, 7, 7, 8, 8, 10], 8)
