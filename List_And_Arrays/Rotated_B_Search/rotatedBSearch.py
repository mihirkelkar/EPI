def rotatedBSearch(array, num):
  low = 0
  high = len(array) - 1
  while low <= high:
    middle = (low + high) / 2
    if array[middle] == num:
      return True
    elif array[middle] > num:
      if array[low] > num:
        low = middle + 1
      else:
        high = middle - 1
    elif array[middle] < num:
      if array[high] < num:
        high = middle - 1
      else:
        low = middle + 1
  return False

print rotatedBSearch([5, 6, 7, 8, 1, 3, 4], 6)
print rotatedBSearch([5, 6, 7, 8, 1, 3, 4], 10)
