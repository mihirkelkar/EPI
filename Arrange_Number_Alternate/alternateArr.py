def alternate(array):
  for ii in range(1, len(array)):
    if ii % 2 and array[ii] < array[ii - 1]:
      array[ii - 1], array[ii] = array[ii], array[ii - 1]
    if ii % 2 == 0 and array[ii] > array[ii - 1]:
      array[ii - 1], array[ii] = array[ii], array[ii - 1]
  return array


print alternate([1, 2, 3, 4, 5, 6])
