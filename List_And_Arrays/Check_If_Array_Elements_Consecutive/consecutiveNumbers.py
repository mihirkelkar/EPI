import collections

def findIfConsecutive(array):
  num_dict = collections.defaultdict(int)
  max = -float("inf")
  min = float("inf")
  for ii in array:
    if ii > max:
      max = ii
    if ii < min:
      min = ii
    num_dict[ii] += 1
  print num_dict
  if max - min + 1 == len(array):
    if sum(num_dict.values()) == len(array):
      return True
  return False
  
print findIfConsecutive([5, 3, 4, 1, 2])
print findIfConsecutive([79, 77, 80, 76, 81])
