def mergeInterval(array):
  sorted_intervals = sorted(array, key = lambda x : x[0])
  new_list = list()
  for ii in sorted_intervals:
    if not new_list:
      new_list.append(ii)
    else:
      if new_list[-1][1] >= ii[0]:
        new_list[-1][1] = ii[1]
      else:
        new_list.append(ii)
  print new_list

mergeInterval([[1, 3], [2, 6], [8, 10], [15, 18]])  
