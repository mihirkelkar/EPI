import collections

def sortDict(string, dict_string): 
  temp = collections.defaultdict(int)
  for index, ii in enumerate(dict_string):
    temp[ii] = index

  freq_counter = collections.defaultdict(int)
  for ii in string:
    freq_counter[ii] += 1
  
  new_string = ''
  for ii in sorted(temp.items(), key = lambda x: x[1]):
    if ii[0] in freq_counter:
      new_string = new_string + ii[0] * freq_counter[ii[0]]
  print new_string 
sortDict('abccbaabc', 'cba') 
