def rotate(arr, d):
  arr = reverseArray(arr, 0, len(arr)-1)
  arr = reverseArray(arr, 0, len(arr) - d - 1)
  arr = reverseArray(arr, len(arr) - d, len(arr) - 1)
  return arr


def reverseArray(arr, start, end):
  while start <= end:
    arr[start], arr[end] = arr[end], arr[start]
    start += 1
    end -= 1
  return arr

print rotate([1, 2, 3, 4, 5, 6, 7], 2)
