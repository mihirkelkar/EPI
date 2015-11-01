def unknownSearch(array, number):
  index = 2
  while True:
    try:
      if array[index] > number:
        return binarySearch(array[0:index+ 1], number)
      else:
        index *= 2
    except:
      return -1

def binarySearch(array, number):
  low = 0
  high = len(array)
  while low <= high:
    middle = (low + high) // 2
    if number == array[middle]:
      return middle
    elif number < array[middle]:
      high = middle 
    elif number > array[middle]:
      low = middle
  return -1

print unknownSearch([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14], 4)
