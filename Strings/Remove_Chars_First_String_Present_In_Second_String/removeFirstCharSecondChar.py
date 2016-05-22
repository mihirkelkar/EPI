import collections

def removeChars(string_one, string_two):
  temp_hash = collections.defaultdict(int)
  for ii in string_one:
    temp_hash[ii] += 1
  for ii in string_two:
    try:
      del temp_hash[ii]
    except:
      pass
  res = ''
  for ii in string_one:
    if ii in temp_hash:
      res += ii 
  return res


print removeChars('test string', 'mask')
