def searchSorted(array):
  low = 0
  high = len(array) - 1
  while  low <= high:
    mid = (low + high) / 2
    val = array[mid] - mid
    if val == 0:
      return mid
    elif val > 0:
      high = mid - 1
    elif val < 0:
      low = mid + 1
  return -1

print searchSorted([-2, -1, 0, 2, 4, 6, 9])
print searchSorted([-2, -1, 0])
