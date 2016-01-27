import collections
def efficientPerm(string):
  temp = collections.defaultdict(int)
  for ii in string:
    temp[ii] += 1
  count = 0
  for ii in temp.values():
    if ii % 2 == 1:
      count += 1
  if count > 1:
    return False
  return True


print efficientPerm('civic')
print efficientPerm('racecar')
print efficientPerm('goodrx')
