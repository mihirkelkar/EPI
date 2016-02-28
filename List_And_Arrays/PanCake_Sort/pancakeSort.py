def flip(array, ii):
  counter = 0
  while counter < ii:
    temp = array[ii]
    array[ii] = array[counter]
    array[counter] = temp
    counter += 1
    ii -= 1
  return array

def findMax(array, currentSize):
  result = -float("inf")
  index = 0
  for ii in range(0, currentSize):
    if array[ii] > result:
      result = array[ii]
      index = ii
  return index

def panCake(array):
  ii = len(array)
  while ii >= 1:
    max = findMax(array, ii)
    array = flip(array, max)
    array = flip(array, ii-1)
    print array
    ii -= 1
  print "--------"
  print array
  print "--------"

panCake([23, 10, 20, 11, 12, 6, 7])
    
