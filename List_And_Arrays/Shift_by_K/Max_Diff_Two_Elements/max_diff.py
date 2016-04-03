def maxDiffNaive(array):
  max_diff = 0
  for ii in range(0, len(array)):
    for jj in range(ii + 1, len(array)):
      if array[jj] > array[ii]:
        if array[jj] - array[ii] > max_diff:
          max_diff = array[jj] - array[ii]
  print max_diff


def maxDiff(array):
  min_so_far = array[0]
  max_diff = 0
  for ii in range(1, len(array)):
    if array[ii] <= min_so_far:
      min_so_far = array[ii]
    else:
      if array[ii] - min_so_far > max_diff:
        max_diff = array[ii] - min_so_far
  print max_diff  


maxDiff([1, 2, 90, 10, 110])
