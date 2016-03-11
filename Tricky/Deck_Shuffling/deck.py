import random

def deck(array):
  for ii in range(0, len(array)):
    temp = random.randint(ii, len(array)-1) 
    array[ii], array[temp] = array[temp], array[ii]
  return array

print deck([1, 2, 3, 4, 5])  
