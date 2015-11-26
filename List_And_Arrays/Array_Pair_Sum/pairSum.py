#this function explores the binary search solution for the pair sum problem

def pairBinarySearch(array, k):
  #Sort the array
  array.sort()
  for ii in array:
    if binary_search(array, k - ii):
      print ii, k-ii

def binary_search(array, num):
  low = 0
  high = len(array) - 1
  while low <= high:
    middle = (low + high) // 2
    if num == array[middle]:
      return True
    elif num < array[middle]:
      high = middle - 1
    elif num > array[middle]:
      low = middle + 1

#This function now solves the same Problem in Linear Time
def pairLinearTime(array, k):
  hash = {}
  for ii in array:
    if ii not in hash:
      hash[ii] = 1
    else:
      hash[ii] += 1
  for ii in array:
    try:
      temp = hash[k-ii]
      if ii == k-ii:
        if temp > 1:
          print ii, k - ii
      else:
        print ii, k-ii
    except:
      continue

pairLinearTime([1, 3, 4, 5, 7, 2, 6], 8)
print '---'
pairBinarySearch([1, 3, 4, 5, 7, 2, 6], 8)    
