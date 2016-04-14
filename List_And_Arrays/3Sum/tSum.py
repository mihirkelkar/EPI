import collections
def tSum(array):
  sorted_array = sorted(array)
  dict_num = collections.defaultdict(list)
  for index, ii in enumerate(sorted_array):
    dict_num[ii].append(index)
  for ii in range(0, len(sorted_array)):
    for jj in range(ii + 1, len(sorted_array)):
      temp = -1 * (sorted_array[ii] + sorted_array[jj])
      if temp in dict_num:
        if dict_num[temp][0] > jj:
          print sorted_array[ii], sorted_array[jj], temp
   

tSum([-1, 0, 1, 2, -1, -4])      
