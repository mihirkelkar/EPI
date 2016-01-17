def longestContaining(array):
  hashTable = {}
  for ii in range(0, len(array)):
    hashTable[array[ii]] = ii 
  
  for ii in array:
    print ii
    flag = 0
    size = 1
    upSize = 1
    downSize = 1
    containSize = list()
    #Go Upper
    while True:
      try:
        temp = hashTable[ii + upSize]
        containSize.append(ii + upSize)
        upSize += 1
      except:
        break
        
    while True:
      try:
        temp = hashTable[ii - downSize]
        containSize.append(ii - downSize)
        downSize += 1
        if downSize == upSize:
          flag = 1
          break
      except:
        break
    if flag:
      print containSize
      print '-----------'
longestContaining([3, -2, 7, 9, 1, 2, 0, -1, 5, 8])
