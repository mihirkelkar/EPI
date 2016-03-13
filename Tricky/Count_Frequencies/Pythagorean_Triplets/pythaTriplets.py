import math

def pythaTriplets(array):
  array = [ii * ii for ii in array]
  hashmap = {}
  for ii in array:
    hashmap[ii] = 1
  sorted_a = sorted(array)
  for ii in range(len(sorted_a)):
    for jj in range(ii+1, len(sorted_a)):
      try:
        temp = hashmap[sorted_a[ii] + sorted_a[jj]]
        print (math.sqrt(sorted_a[ii]), math.sqrt(sorted_a[jj]), math.sqrt(sorted_a[ii] + sorted_a[jj]))
      except:
        pass

pythaTriplets([3, 1, 4, 6, 5])
