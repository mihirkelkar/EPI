def productArray(array):
  left_array = [1]
  for ii in range(1, len(array)):
    new_element = left_array[-1] * array[ii - 1]
    left_array.append(new_element)
  right_array = [1]
  for ii in range(1, len(array)):
    new_element = right_array[-1] * array[len(array)  - ii]
    right_array.append(new_element)
  return [left_array[ii] * right_array[len(array) - 1 - ii] for ii in range(0, len(array))]

print productArray([10, 3, 5, 6, 2])

