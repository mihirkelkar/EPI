def threeNumSort(array):
  min = 0
  max = len(array) - 1
  while array[min] == -1:
    min += 1
  while array[max] == 1:
    max -= 1
  start = min + 1
  while start <= max:
    if array[start] == -1:
      array[min], array[start] = array[start], array[min]
      while array[min] == -1:
        min += 1
      start = min + 1
    elif array[start] == 1:
      array[max], array[start] = array[start], array[max]
      while array[max] == 1:
        max -= 1
    elif array[start] == 0:
      start += 1  
       
  return array

print threeNumSort([0, -1, 1, 1, 0, -1, 0, -1, 1, 1, -1, 0, 1, 0, 0, 1])

