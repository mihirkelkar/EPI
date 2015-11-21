def binarySearchMod(array, k):
  low = 0
  high = len(array)
  while low < high:
    middle = (low + high) / 2
    if array[middle] == k:
      index = binarySearchMod(array[:middle], k)
      if index == -1:
        return middle
      return index
    elif array[middle] > k:
      high = middle - 1
    
    elif array[middle] < k:
      low = middle + 1
  return -1

print binarySearchMod([1, 2, 2, 3,4,4,5], 4)
