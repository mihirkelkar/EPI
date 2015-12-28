def twoSum(array, number):
  numDict = {}
  for ii in range(0, len(array)):
    numDict[array[ii]] = ii
  for ii in array:
    try:
      x = numDict[number - ii]
      return (numDict[ii], x)
    except:
      pass

print twoSum([2, 7, 1, 15], 9)
