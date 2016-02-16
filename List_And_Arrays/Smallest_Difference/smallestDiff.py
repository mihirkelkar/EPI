import math 

def smallestDiff(list_a, list_b):
  ii = len(list_a)
  jj = len(list_b)
  list_a = sorted(list_a)
  list_b = sorted(list_b)
  min_so_far = float("inf")
  counter_a = counter_b = 0
  while counter_a < ii and counter_b < jj:
    min = list_a[counter_a] - list_b[counter_b]
    if min < 0:
      counter_a += 1
    else:
      counter_b += 1
    if math.fabs(min) < min_so_far:
      min_so_far = math.fabs(min)
  return min_so_far  

print smallestDiff([1, 2, 11, 15], [4, 12, 19, 23, 127, 235])
