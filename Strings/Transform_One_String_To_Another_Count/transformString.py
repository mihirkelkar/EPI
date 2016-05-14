def transformString(string_one, string_two):
  if len(string_one) != len(string_two):
    return False
  count = [0] * 256
  for ii in xrange(len(string_one)):
    count[ord(string_one[ii].lower())] += 1
  for ii in xrange(len(string_two)):
    count[ord(string_two[ii].lower())] -= 1
  for ii in range(256):
    if count[ii] != 0:
      return False

  res = 0
  ii = len(string_one)-1
  jj = len(string_two)-1
  while ii >= 0:
    if string_one[ii] == string_two[jj]:
      ii -= 1
      jj -= 1
    else:
      ii -= 1
      res += 1
  return res

print transformString("EACBD", "EABCD")
  
