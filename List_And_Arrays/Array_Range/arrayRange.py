def arrayRange(array):
  array = sorted(array, key = lambda x : x[0])
  new_array = []
  for ii in range(1, len(array)):
    if array[ii][0] == array[ii - 1][0]:
      if array[ii][1] > array[ii - 1][1]:
        new_array.append(array[ii])
        if ii != len(array) - 1:
          ii += 1
        else:
          break
    #Since array is sorted we are not worrying about the case where x + 1 < x
    else:
      if array[ii][1] <= array[ii - 1][1]:
        new_array.append(array[ii - 1])
  return new_array

print arrayRange([(2, 6), (3, 5), (7, 21), (20, 21)])
