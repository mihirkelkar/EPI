def arithematicProgress(numbers):
  low = 0
  high = len(numbers) - 1
  ap = (numbers[high] - numbers[low]) / len(numbers)
  while low < high:
    middle = (low + high) / 2
    if numbers[middle] == numbers[low] + ap * middle:
      low = middle + 1
    elif numbers[middle] > numbers[low] + ap * middle:
      if numbers[middle-1] == numbers[low] + ap * (middle-1):
        return numbers[low] + ap * middle
      else:
        high = middle - 1
  return -1


print arithematicProgress([1, 7, 10, 13, 16, 19, 22])
