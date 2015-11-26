def largest_contiguous_sum(array):
  if len(array) == 0:
    return 0
  max_sum = current_sum = array[0]
  for ii in array[1:]:
    current_sum = max(current_sum + ii, ii)
    max_sum = max(current_sum, max_sum)
  return max_sum

def largest_contiguous_sum_modi(array):
  #lets modify the same function to also return the start and the end point
  #of the contiguous sequence here. 
  start_point = 0
  end_point = 0
  start = end = 0
  if len(array) == 0:
    return 0, start_point, end_point
  max_sum = current_sum = array[0]
  for ii in range(1, len(array) - 1):
    if current_sum + array[ii] >= array[ii]:
      end_point = ii
      current_sum += array[ii]
    else:  
      current_sum = array[ii]
      start_point = ii
      end_point = ii
    if current_sum > max_sum:
      max_sum = current_sum
      start = start_point
      end = end_point
  return max_sum, start_point, end_point    


def main():
  print largest_contiguous_sum([1, 2, 3, 4, 5, -6])
  print largest_contiguous_sum_modi([1, 2, 3, 4, 5, -6])
if __name__ == "__main__":
  main()
