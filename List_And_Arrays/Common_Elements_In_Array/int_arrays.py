def common_ints(array_one, array_two):
  array_one = sorted(array_one)
  array_two = sorted(array_two)
  counter_one = 0
  counter_two = 0
  common_elements = list()
  while counter_one < len(array_one) and counter_two < len(array_two):
    if array_one[counter_one] == array_two[counter_two]:
      common_elements.append(array_one[counter_one])
      counter_one += 1
      counter_two += 1
    elif array_one[counter_one] < array_two[counter_two]:
      counter_one += 1
    elif array_one[counter_one] > array_two[counter_two]:
      counter_two += 1
  return common_elements

print common_ints([1, 2, 3, 4], [3, 4, 5, 6])
print common_ints([1, 2, 3, 4], [1, 2, 3, 4, 5, 6])  
