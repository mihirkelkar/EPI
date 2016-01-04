def search(array, k):
  low = 0
  high = len(array) - 1
  while low <= high:
    mid = (low + high) / 2
    if array[mid] == k:
      retval = search(array[low:mid], k)
      if retval != -1:
        return retval
      return mid
    elif array[mid] > k:
      high = mid - 1
    elif array[mid] < k:
      low = mid + 1
  return -1

print search([0, 0, 1, 2, 2, 3, 4, 5], 0)
