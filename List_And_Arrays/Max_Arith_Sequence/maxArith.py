def maxArith(array):
  count = 1
  max_count = 0
  prev_diff = None
  for ii in range(1, len(array)):
    diff = array[ii] - array[ii - 1]
    if diff == prev_diff or prev_diff == None:
      count += 1
    else:
      if count > max_count:
        max_count = count
      count = 2
    prev_diff = diff
  if count > max_count:
    max_count = count
  print max_count

maxArith([1, 6, 7, 8, 9, 4, 3, 2, 1, 0])

