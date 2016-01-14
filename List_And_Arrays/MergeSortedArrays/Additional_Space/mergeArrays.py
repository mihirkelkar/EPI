def mergeArrays(a, b):
  newList = list()
  while len(a) != 0 and len(b) != 0:
    if a[0] < b[0]:
      newList.append(a.pop(0))
    else:
      newList.append(b.pop(0))
  if len(a) > 0:
    newList += a
  else:
    newList += b

  return newList

print mergeArrays([1, 2, 3], [10, 14, 15])
