def indexToSort(array):
  ii = 0
  jj = len(array) - 1
  flag = [0, 0]
  while ii < jj:
    if array[ii] <= array[ii + 1]:
      ii += 1
    else:
      flag[0] = 1
    if array[jj - 1] <= array[jj]:
      jj -= 1
    else:
      flag[1] = 1
    if flag == [1, 1]:
      break
  if ii < jj:
    min_middle = min(array[ii+1:jj])
    max_middle = min(array[ii+1:jj])
    while array[ii] > min_middle:
      ii -= 1
    while array[jj] < max_middle:
      jj += 1
    return (ii, jj)
  return (0, len(array) - 1)

print indexToSort([1, 2, 4, 7, 10, 11, 7,12, 6, 7, 16, 18, 19])
print indexToSort([1, 2, 4, 7, 10, 11, 8, 12, 5, 6, 16, 18, 19])
