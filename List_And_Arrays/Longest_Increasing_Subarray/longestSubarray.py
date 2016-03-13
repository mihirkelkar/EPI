def longestSubarray(array):
  longest_so_far = 1
  start = 0
  end = 0
  cur_longest = 1
  for ii in range(1, len(array)):
    if array[ii] > array[ii - 1]:
      cur_longest += 1
      end = ii
      if cur_longest > longest_so_far:
        longest_so_far = cur_longest
    else:
      cur_longest = 1
      start = ii
      end = ii
  print longest_so_far
  print start
  print end


longestSubarray([1, 2, 3, 3, 2, 4, 6, 7])      
